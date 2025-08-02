_A3='oxcConfGroupV4'
_A2='oxcIfGroupV4'
_A1='oxcIfGroupV3'
_A0='oxcGeneralGroupV3'
_z='oxcConfGroup'
_y='oxcIfGroup'
_x='oxcConfObjectProperty'
_w='oxcIfObjectProperty'
_v='oxcGeneralOxcConfTableSize'
_u='oxcGeneralOxcIfTableSize'
_t='oxcConfRowStatus'
_s='oxcIfAdminStatus'
_r='oxcGeneralMibImplVersion'
_q='oxcGeneralMibSpecVersion'
_p='oxcGeneralTestAndIncr'
_o='read-create'
_n='PortNumber'
_m='oxcGeneralGroupV4'
_l='oxcGeneralGroupV2'
_k='oxcConfGroupV2'
_j='oxcGeneralGroup'
_i='oxcIfIsReserved'
_h='oxcGeneralStateLastChangeTime'
_g='oxcConfOperStatus'
_f='oxcConfGroupV3'
_e='oxcConfServiceFailure'
_d='up'
_c='down'
_b='Unsigned32'
_a='oxcIfGroupV2'
_Z='oxcConfAdminStatus'
_Y='oxcConfLastChangeTime'
_X='oxcConfOutPort'
_W='oxcConfInPort'
_V='oxcConfSlot'
_U='oxcConfSubrack'
_T='oxcConfDescr'
_S='oxcConfName'
_R='oxcIfOperStatus'
_Q='oxcIfDirection'
_P='oxcIfInvPhysIndexOrZero'
_O='oxcIfPort'
_N='oxcIfSlot'
_M='oxcIfSubrack'
_L='oxcIfDescr'
_K='oxcIfName'
_J='oxcGeneralLastChangeTime'
_I='DisplayString'
_H='oxcConfIndex'
_G='oxcIfIndex'
_F='Integer32'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-OXC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumOxcMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumOxcMIB')
FaultStatus,MgmtNameString,ObjectProperty,PortNumber,PortType,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC','FaultStatus','MgmtNameString','ObjectProperty',_n,'PortType','SlotNumber','SubrackNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_b,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'PhysAddress','RowStatus','TextualConvention','TestAndIncr')
lumOxcMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,11))
if mibBuilder.loadTexts:lumOxcMIBModule.setRevisions(('2017-06-15 00:00','2016-01-11 00:00','2008-05-12 00:00','2002-03-26 00:00','2001-12-11 00:00','2001-10-30 00:00','2001-10-11 00:00','2001-09-04 00:00','2001-08-24 00:00'))
_LumOxcConfs_ObjectIdentity=ObjectIdentity
lumOxcConfs=_LumOxcConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,10,1))
_LumOxcGroups_ObjectIdentity=ObjectIdentity
lumOxcGroups=_LumOxcGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,10,1,1))
_LumOxcCompl_ObjectIdentity=ObjectIdentity
lumOxcCompl=_LumOxcCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,10,1,2))
_LumOxcMIBObjects_ObjectIdentity=ObjectIdentity
lumOxcMIBObjects=_LumOxcMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,10,2))
_OxcGeneral_ObjectIdentity=ObjectIdentity
oxcGeneral=_OxcGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,10,2,1))
_OxcGeneralTestAndIncr_Type=TestAndIncr
_OxcGeneralTestAndIncr_Object=MibScalar
oxcGeneralTestAndIncr=_OxcGeneralTestAndIncr_Object((1,3,6,1,4,1,8708,2,10,2,1,1),_OxcGeneralTestAndIncr_Type())
oxcGeneralTestAndIncr.setMaxAccess(_E)
if mibBuilder.loadTexts:oxcGeneralTestAndIncr.setStatus(_B)
class _OxcGeneralMibSpecVersion_Type(DisplayString):defaultValue=OctetString('')
_OxcGeneralMibSpecVersion_Type.__name__=_I
_OxcGeneralMibSpecVersion_Object=MibScalar
oxcGeneralMibSpecVersion=_OxcGeneralMibSpecVersion_Object((1,3,6,1,4,1,8708,2,10,2,1,2),_OxcGeneralMibSpecVersion_Type())
oxcGeneralMibSpecVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:oxcGeneralMibSpecVersion.setStatus(_B)
class _OxcGeneralMibImplVersion_Type(DisplayString):defaultValue=OctetString('')
_OxcGeneralMibImplVersion_Type.__name__=_I
_OxcGeneralMibImplVersion_Object=MibScalar
oxcGeneralMibImplVersion=_OxcGeneralMibImplVersion_Object((1,3,6,1,4,1,8708,2,10,2,1,3),_OxcGeneralMibImplVersion_Type())
oxcGeneralMibImplVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:oxcGeneralMibImplVersion.setStatus(_B)
_OxcGeneralLastChangeTime_Type=DateAndTime
_OxcGeneralLastChangeTime_Object=MibScalar
oxcGeneralLastChangeTime=_OxcGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,10,2,1,4),_OxcGeneralLastChangeTime_Type())
oxcGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcGeneralLastChangeTime.setStatus(_B)
_OxcGeneralStateLastChangeTime_Type=DateAndTime
_OxcGeneralStateLastChangeTime_Object=MibScalar
oxcGeneralStateLastChangeTime=_OxcGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,10,2,1,5),_OxcGeneralStateLastChangeTime_Type())
oxcGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcGeneralStateLastChangeTime.setStatus(_B)
_OxcGeneralOxcIfTableSize_Type=Unsigned32
_OxcGeneralOxcIfTableSize_Object=MibScalar
oxcGeneralOxcIfTableSize=_OxcGeneralOxcIfTableSize_Object((1,3,6,1,4,1,8708,2,10,2,1,6),_OxcGeneralOxcIfTableSize_Type())
oxcGeneralOxcIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcGeneralOxcIfTableSize.setStatus(_B)
_OxcGeneralOxcConfTableSize_Type=Unsigned32
_OxcGeneralOxcConfTableSize_Object=MibScalar
oxcGeneralOxcConfTableSize=_OxcGeneralOxcConfTableSize_Object((1,3,6,1,4,1,8708,2,10,2,1,7),_OxcGeneralOxcConfTableSize_Type())
oxcGeneralOxcConfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcGeneralOxcConfTableSize.setStatus(_B)
_OxcIfList_ObjectIdentity=ObjectIdentity
oxcIfList=_OxcIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,10,2,2))
_OxcIfTable_Object=MibTable
oxcIfTable=_OxcIfTable_Object((1,3,6,1,4,1,8708,2,10,2,2,1))
if mibBuilder.loadTexts:oxcIfTable.setStatus(_B)
_OxcIfEntry_Object=MibTableRow
oxcIfEntry=_OxcIfEntry_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1))
oxcIfEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:oxcIfEntry.setStatus(_B)
class _OxcIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OxcIfIndex_Type.__name__=_b
_OxcIfIndex_Object=MibTableColumn
oxcIfIndex=_OxcIfIndex_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,1),_OxcIfIndex_Type())
oxcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfIndex.setStatus(_B)
_OxcIfName_Type=MgmtNameString
_OxcIfName_Object=MibTableColumn
oxcIfName=_OxcIfName_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,2),_OxcIfName_Type())
oxcIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfName.setStatus(_B)
class _OxcIfDescr_Type(DisplayString):defaultValue=OctetString('')
_OxcIfDescr_Type.__name__=_I
_OxcIfDescr_Object=MibTableColumn
oxcIfDescr=_OxcIfDescr_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,3),_OxcIfDescr_Type())
oxcIfDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:oxcIfDescr.setStatus(_B)
_OxcIfSubrack_Type=SubrackNumber
_OxcIfSubrack_Object=MibTableColumn
oxcIfSubrack=_OxcIfSubrack_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,4),_OxcIfSubrack_Type())
oxcIfSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfSubrack.setStatus(_B)
_OxcIfSlot_Type=SlotNumber
_OxcIfSlot_Object=MibTableColumn
oxcIfSlot=_OxcIfSlot_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,5),_OxcIfSlot_Type())
oxcIfSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfSlot.setStatus(_B)
_OxcIfPort_Type=PortNumber
_OxcIfPort_Object=MibTableColumn
oxcIfPort=_OxcIfPort_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,6),_OxcIfPort_Type())
oxcIfPort.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfPort.setStatus(_B)
class _OxcIfInvPhysIndexOrZero_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OxcIfInvPhysIndexOrZero_Type.__name__=_b
_OxcIfInvPhysIndexOrZero_Object=MibTableColumn
oxcIfInvPhysIndexOrZero=_OxcIfInvPhysIndexOrZero_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,7),_OxcIfInvPhysIndexOrZero_Type())
oxcIfInvPhysIndexOrZero.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfInvPhysIndexOrZero.setStatus(_B)
_OxcIfDirection_Type=PortType
_OxcIfDirection_Object=MibTableColumn
oxcIfDirection=_OxcIfDirection_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,8),_OxcIfDirection_Type())
oxcIfDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfDirection.setStatus(_B)
class _OxcIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('undefined',0),(_c,1),(_d,2)))
_OxcIfAdminStatus_Type.__name__=_F
_OxcIfAdminStatus_Object=MibTableColumn
oxcIfAdminStatus=_OxcIfAdminStatus_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,9),_OxcIfAdminStatus_Type())
oxcIfAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oxcIfAdminStatus.setStatus(_D)
class _OxcIfOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPresent',1),(_c,2),(_d,3)))
_OxcIfOperStatus_Type.__name__=_F
_OxcIfOperStatus_Object=MibTableColumn
oxcIfOperStatus=_OxcIfOperStatus_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,10),_OxcIfOperStatus_Type())
oxcIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfOperStatus.setStatus(_B)
class _OxcIfIsReserved_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_OxcIfIsReserved_Type.__name__=_F
_OxcIfIsReserved_Object=MibTableColumn
oxcIfIsReserved=_OxcIfIsReserved_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,11),_OxcIfIsReserved_Type())
oxcIfIsReserved.setMaxAccess(_o)
if mibBuilder.loadTexts:oxcIfIsReserved.setStatus(_B)
_OxcIfObjectProperty_Type=ObjectProperty
_OxcIfObjectProperty_Object=MibTableColumn
oxcIfObjectProperty=_OxcIfObjectProperty_Object((1,3,6,1,4,1,8708,2,10,2,2,1,1,12),_OxcIfObjectProperty_Type())
oxcIfObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcIfObjectProperty.setStatus(_B)
_OxcConfList_ObjectIdentity=ObjectIdentity
oxcConfList=_OxcConfList_ObjectIdentity((1,3,6,1,4,1,8708,2,10,2,3))
_OxcConfTable_Object=MibTable
oxcConfTable=_OxcConfTable_Object((1,3,6,1,4,1,8708,2,10,2,3,1))
if mibBuilder.loadTexts:oxcConfTable.setStatus(_B)
_OxcConfEntry_Object=MibTableRow
oxcConfEntry=_OxcConfEntry_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1))
oxcConfEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:oxcConfEntry.setStatus(_B)
class _OxcConfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OxcConfIndex_Type.__name__=_b
_OxcConfIndex_Object=MibTableColumn
oxcConfIndex=_OxcConfIndex_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,1),_OxcConfIndex_Type())
oxcConfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfIndex.setStatus(_B)
_OxcConfName_Type=MgmtNameString
_OxcConfName_Object=MibTableColumn
oxcConfName=_OxcConfName_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,2),_OxcConfName_Type())
oxcConfName.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfName.setStatus(_B)
class _OxcConfDescr_Type(DisplayString):defaultValue=OctetString('')
_OxcConfDescr_Type.__name__=_I
_OxcConfDescr_Object=MibTableColumn
oxcConfDescr=_OxcConfDescr_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,3),_OxcConfDescr_Type())
oxcConfDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:oxcConfDescr.setStatus(_B)
_OxcConfSubrack_Type=SubrackNumber
_OxcConfSubrack_Object=MibTableColumn
oxcConfSubrack=_OxcConfSubrack_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,4),_OxcConfSubrack_Type())
oxcConfSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfSubrack.setStatus(_B)
_OxcConfSlot_Type=SlotNumber
_OxcConfSlot_Object=MibTableColumn
oxcConfSlot=_OxcConfSlot_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,5),_OxcConfSlot_Type())
oxcConfSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfSlot.setStatus(_B)
_OxcConfInPort_Type=PortNumber
_OxcConfInPort_Object=MibTableColumn
oxcConfInPort=_OxcConfInPort_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,6),_OxcConfInPort_Type())
oxcConfInPort.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfInPort.setStatus(_B)
class _OxcConfOutPort_Type(PortNumber):defaultValue=0
_OxcConfOutPort_Type.__name__=_n
_OxcConfOutPort_Object=MibTableColumn
oxcConfOutPort=_OxcConfOutPort_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,7),_OxcConfOutPort_Type())
oxcConfOutPort.setMaxAccess(_E)
if mibBuilder.loadTexts:oxcConfOutPort.setStatus(_B)
_OxcConfLastChangeTime_Type=DateAndTime
_OxcConfLastChangeTime_Object=MibTableColumn
oxcConfLastChangeTime=_OxcConfLastChangeTime_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,8),_OxcConfLastChangeTime_Type())
oxcConfLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfLastChangeTime.setStatus(_B)
class _OxcConfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_OxcConfAdminStatus_Type.__name__=_F
_OxcConfAdminStatus_Object=MibTableColumn
oxcConfAdminStatus=_OxcConfAdminStatus_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,9),_OxcConfAdminStatus_Type())
oxcConfAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oxcConfAdminStatus.setStatus(_B)
class _OxcConfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_OxcConfOperStatus_Type.__name__=_F
_OxcConfOperStatus_Object=MibTableColumn
oxcConfOperStatus=_OxcConfOperStatus_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,10),_OxcConfOperStatus_Type())
oxcConfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfOperStatus.setStatus(_D)
_OxcConfRowStatus_Type=RowStatus
_OxcConfRowStatus_Object=MibTableColumn
oxcConfRowStatus=_OxcConfRowStatus_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,11),_OxcConfRowStatus_Type())
oxcConfRowStatus.setMaxAccess(_o)
if mibBuilder.loadTexts:oxcConfRowStatus.setStatus(_D)
_OxcConfServiceFailure_Type=FaultStatus
_OxcConfServiceFailure_Object=MibTableColumn
oxcConfServiceFailure=_OxcConfServiceFailure_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,12),_OxcConfServiceFailure_Type())
oxcConfServiceFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfServiceFailure.setStatus(_B)
_OxcConfObjectProperty_Type=ObjectProperty
_OxcConfObjectProperty_Object=MibTableColumn
oxcConfObjectProperty=_OxcConfObjectProperty_Object((1,3,6,1,4,1,8708,2,10,2,3,1,1,13),_OxcConfObjectProperty_Type())
oxcConfObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:oxcConfObjectProperty.setStatus(_B)
oxcGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,1))
oxcGeneralGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_J)))
if mibBuilder.loadTexts:oxcGeneralGroup.setStatus(_D)
oxcIfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,2))
oxcIfGroup.setObjects(*((_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_s),(_A,_R)))
if mibBuilder.loadTexts:oxcIfGroup.setStatus(_D)
oxcConfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,3))
oxcConfGroup.setObjects(*((_A,_H),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_g),(_A,_t)))
if mibBuilder.loadTexts:oxcConfGroup.setStatus(_D)
oxcIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,4))
oxcIfGroupV2.setObjects(*((_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:oxcIfGroupV2.setStatus(_D)
oxcConfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,5))
oxcConfGroupV2.setObjects(*((_A,_H),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_g),(_A,_e)))
if mibBuilder.loadTexts:oxcConfGroupV2.setStatus(_D)
oxcGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,6))
oxcGeneralGroupV2.setObjects((_A,_J))
if mibBuilder.loadTexts:oxcGeneralGroupV2.setStatus(_D)
oxcConfGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,7))
oxcConfGroupV3.setObjects(*((_A,_H),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_e)))
if mibBuilder.loadTexts:oxcConfGroupV3.setStatus(_D)
oxcGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,8))
oxcGeneralGroupV3.setObjects(*((_A,_J),(_A,_h)))
if mibBuilder.loadTexts:oxcGeneralGroupV3.setStatus(_D)
oxcIfGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,9))
oxcIfGroupV3.setObjects(*((_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_i)))
if mibBuilder.loadTexts:oxcIfGroupV3.setStatus(_D)
oxcGeneralGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,10))
oxcGeneralGroupV4.setObjects(*((_A,_J),(_A,_h),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:oxcGeneralGroupV4.setStatus(_B)
oxcIfGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,11))
oxcIfGroupV4.setObjects(*((_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_i),(_A,_w)))
if mibBuilder.loadTexts:oxcIfGroupV4.setStatus(_B)
oxcConfGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,10,1,1,12))
oxcConfGroupV4.setObjects(*((_A,_H),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_e),(_A,_x)))
if mibBuilder.loadTexts:oxcConfGroupV4.setStatus(_B)
lumOxcBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,10,1,2,1))
lumOxcBasicComplV1.setObjects(*((_A,_j),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:lumOxcBasicComplV1.setStatus(_D)
lumOxcBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,10,1,2,2))
lumOxcBasicComplV2.setObjects(*((_A,_j),(_A,_a),(_A,_k)))
if mibBuilder.loadTexts:lumOxcBasicComplV2.setStatus(_D)
lumOxcBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,10,1,2,3))
lumOxcBasicComplV3.setObjects(*((_A,_l),(_A,_a),(_A,_k)))
if mibBuilder.loadTexts:lumOxcBasicComplV3.setStatus(_D)
lumOxcBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,10,1,2,4))
lumOxcBasicComplV4.setObjects(*((_A,_l),(_A,_a),(_A,_f)))
if mibBuilder.loadTexts:lumOxcBasicComplV4.setStatus(_D)
lumOxcBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,10,1,2,5))
lumOxcBasicComplV5.setObjects(*((_A,_A0),(_A,_a),(_A,_f)))
if mibBuilder.loadTexts:lumOxcBasicComplV5.setStatus(_D)
lumOxcBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,10,1,2,6))
lumOxcBasicComplV6.setObjects(*((_A,_m),(_A,_A1),(_A,_f)))
if mibBuilder.loadTexts:lumOxcBasicComplV6.setStatus(_D)
lumOxcBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,10,1,2,7))
lumOxcBasicComplV7.setObjects(*((_A,_m),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:lumOxcBasicComplV7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumOxcMIBModule':lumOxcMIBModule,'lumOxcConfs':lumOxcConfs,'lumOxcGroups':lumOxcGroups,_j:oxcGeneralGroup,_y:oxcIfGroup,_z:oxcConfGroup,_a:oxcIfGroupV2,_k:oxcConfGroupV2,_l:oxcGeneralGroupV2,_f:oxcConfGroupV3,_A0:oxcGeneralGroupV3,_A1:oxcIfGroupV3,_m:oxcGeneralGroupV4,_A2:oxcIfGroupV4,_A3:oxcConfGroupV4,'lumOxcCompl':lumOxcCompl,'lumOxcBasicComplV1':lumOxcBasicComplV1,'lumOxcBasicComplV2':lumOxcBasicComplV2,'lumOxcBasicComplV3':lumOxcBasicComplV3,'lumOxcBasicComplV4':lumOxcBasicComplV4,'lumOxcBasicComplV5':lumOxcBasicComplV5,'lumOxcBasicComplV6':lumOxcBasicComplV6,'lumOxcBasicComplV7':lumOxcBasicComplV7,'lumOxcMIBObjects':lumOxcMIBObjects,'oxcGeneral':oxcGeneral,_p:oxcGeneralTestAndIncr,_q:oxcGeneralMibSpecVersion,_r:oxcGeneralMibImplVersion,_J:oxcGeneralLastChangeTime,_h:oxcGeneralStateLastChangeTime,_u:oxcGeneralOxcIfTableSize,_v:oxcGeneralOxcConfTableSize,'oxcIfList':oxcIfList,'oxcIfTable':oxcIfTable,'oxcIfEntry':oxcIfEntry,_G:oxcIfIndex,_K:oxcIfName,_L:oxcIfDescr,_M:oxcIfSubrack,_N:oxcIfSlot,_O:oxcIfPort,_P:oxcIfInvPhysIndexOrZero,_Q:oxcIfDirection,_s:oxcIfAdminStatus,_R:oxcIfOperStatus,_i:oxcIfIsReserved,_w:oxcIfObjectProperty,'oxcConfList':oxcConfList,'oxcConfTable':oxcConfTable,'oxcConfEntry':oxcConfEntry,_H:oxcConfIndex,_S:oxcConfName,_T:oxcConfDescr,_U:oxcConfSubrack,_V:oxcConfSlot,_W:oxcConfInPort,_X:oxcConfOutPort,_Y:oxcConfLastChangeTime,_Z:oxcConfAdminStatus,_g:oxcConfOperStatus,_t:oxcConfRowStatus,_e:oxcConfServiceFailure,_x:oxcConfObjectProperty})