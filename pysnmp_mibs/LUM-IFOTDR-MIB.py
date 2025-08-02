_U='ifOtdrFiberSpanGroupV1'
_T='ifOtdrGeneralGroupV1'
_S='ifOtdrFiberSpanState'
_R='ifOtdrFiberSpanPortNr'
_Q='ifOtdrFiberSpanSlot'
_P='ifOtdrFiberSpanSubrack'
_O='ifOtdrFiberSpanConnIfBasicIfIndex'
_N='ifOtdrFiberSpanStartMeasurementCommand'
_M='ifOtdrFiberSpanSessionType'
_L='ifOtdrFiberSpanFiberId'
_K='ifOtdrFiberSpanName'
_J='ifOtdrGeneralStateLastChangeTime'
_I='ifOtdrGeneralConfigLastChangeTime'
_H='read-write'
_G='DisplayString'
_F='read-create'
_E='ifOtdrFiberSpanIndex'
_D='Integer32'
_C='read-only'
_B='LUM-IFOTDR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfOtdrMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfOtdrMIB','lumModules')
AdminStatusWithNA,CommandString,DisplayStringWithNA,EnabledDisabledWithNA,FaultStatusWithNA,MgmtNameString,OperStatusWithNA,PortNumber,SlotNumber,SubrackNumber,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','AdminStatusWithNA','CommandString','DisplayStringWithNA','EnabledDisabledWithNA','FaultStatusWithNA','MgmtNameString','OperStatusWithNA','PortNumber','SlotNumber','SubrackNumber','Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention')
ifOtdrMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,72))
if mibBuilder.loadTexts:ifOtdrMIBModule.setRevisions(('2018-06-15 00:00',))
_LumIfOtdrConfs_ObjectIdentity=ObjectIdentity
lumIfOtdrConfs=_LumIfOtdrConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,72,1))
_LumIfOtdrGroups_ObjectIdentity=ObjectIdentity
lumIfOtdrGroups=_LumIfOtdrGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,72,1,1))
_LumIfOtdrCompl_ObjectIdentity=ObjectIdentity
lumIfOtdrCompl=_LumIfOtdrCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,72,1,2))
_LumIfOtdrMIBObjects_ObjectIdentity=ObjectIdentity
lumIfOtdrMIBObjects=_LumIfOtdrMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,72,2))
_IfOtdrGeneral_ObjectIdentity=ObjectIdentity
ifOtdrGeneral=_IfOtdrGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,72,2,1))
_IfOtdrGeneralConfigLastChangeTime_Type=DateAndTime
_IfOtdrGeneralConfigLastChangeTime_Object=MibScalar
ifOtdrGeneralConfigLastChangeTime=_IfOtdrGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,72,2,1,1),_IfOtdrGeneralConfigLastChangeTime_Type())
ifOtdrGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtdrGeneralConfigLastChangeTime.setStatus(_A)
_IfOtdrGeneralStateLastChangeTime_Type=DateAndTime
_IfOtdrGeneralStateLastChangeTime_Object=MibScalar
ifOtdrGeneralStateLastChangeTime=_IfOtdrGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,72,2,1,2),_IfOtdrGeneralStateLastChangeTime_Type())
ifOtdrGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtdrGeneralStateLastChangeTime.setStatus(_A)
_IfOtdrGeneralFiberSpanTableSize_Type=Unsigned32
_IfOtdrGeneralFiberSpanTableSize_Object=MibScalar
ifOtdrGeneralFiberSpanTableSize=_IfOtdrGeneralFiberSpanTableSize_Object((1,3,6,1,4,1,8708,2,72,2,1,3),_IfOtdrGeneralFiberSpanTableSize_Type())
ifOtdrGeneralFiberSpanTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtdrGeneralFiberSpanTableSize.setStatus(_A)
_IfOtdrFiberSpanList_ObjectIdentity=ObjectIdentity
ifOtdrFiberSpanList=_IfOtdrFiberSpanList_ObjectIdentity((1,3,6,1,4,1,8708,2,72,2,2))
_IfOtdrFiberSpanTable_Object=MibTable
ifOtdrFiberSpanTable=_IfOtdrFiberSpanTable_Object((1,3,6,1,4,1,8708,2,72,2,2,1))
if mibBuilder.loadTexts:ifOtdrFiberSpanTable.setStatus(_A)
_IfOtdrFiberSpanEntry_Object=MibTableRow
ifOtdrFiberSpanEntry=_IfOtdrFiberSpanEntry_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1))
ifOtdrFiberSpanEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ifOtdrFiberSpanEntry.setStatus(_A)
_IfOtdrFiberSpanIndex_Type=Unsigned32
_IfOtdrFiberSpanIndex_Object=MibTableColumn
ifOtdrFiberSpanIndex=_IfOtdrFiberSpanIndex_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,1),_IfOtdrFiberSpanIndex_Type())
ifOtdrFiberSpanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtdrFiberSpanIndex.setStatus(_A)
_IfOtdrFiberSpanName_Type=MgmtNameString
_IfOtdrFiberSpanName_Object=MibTableColumn
ifOtdrFiberSpanName=_IfOtdrFiberSpanName_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,2),_IfOtdrFiberSpanName_Type())
ifOtdrFiberSpanName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtdrFiberSpanName.setStatus(_A)
class _IfOtdrFiberSpanFiberId_Type(DisplayString):defaultValue=OctetString('')
_IfOtdrFiberSpanFiberId_Type.__name__=_G
_IfOtdrFiberSpanFiberId_Object=MibTableColumn
ifOtdrFiberSpanFiberId=_IfOtdrFiberSpanFiberId_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,3),_IfOtdrFiberSpanFiberId_Type())
ifOtdrFiberSpanFiberId.setMaxAccess(_H)
if mibBuilder.loadTexts:ifOtdrFiberSpanFiberId.setStatus(_A)
class _IfOtdrFiberSpanSessionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nearField',1),('farField',2)))
_IfOtdrFiberSpanSessionType_Type.__name__=_D
_IfOtdrFiberSpanSessionType_Object=MibTableColumn
ifOtdrFiberSpanSessionType=_IfOtdrFiberSpanSessionType_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,4),_IfOtdrFiberSpanSessionType_Type())
ifOtdrFiberSpanSessionType.setMaxAccess(_H)
if mibBuilder.loadTexts:ifOtdrFiberSpanSessionType.setStatus(_A)
_IfOtdrFiberSpanStartMeasurementCommand_Type=CommandString
_IfOtdrFiberSpanStartMeasurementCommand_Object=MibTableColumn
ifOtdrFiberSpanStartMeasurementCommand=_IfOtdrFiberSpanStartMeasurementCommand_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,5),_IfOtdrFiberSpanStartMeasurementCommand_Type())
ifOtdrFiberSpanStartMeasurementCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtdrFiberSpanStartMeasurementCommand.setStatus(_A)
_IfOtdrFiberSpanConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfOtdrFiberSpanConnIfBasicIfIndex_Object=MibTableColumn
ifOtdrFiberSpanConnIfBasicIfIndex=_IfOtdrFiberSpanConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,6),_IfOtdrFiberSpanConnIfBasicIfIndex_Type())
ifOtdrFiberSpanConnIfBasicIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ifOtdrFiberSpanConnIfBasicIfIndex.setStatus(_A)
_IfOtdrFiberSpanSubrack_Type=SubrackNumber
_IfOtdrFiberSpanSubrack_Object=MibTableColumn
ifOtdrFiberSpanSubrack=_IfOtdrFiberSpanSubrack_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,7),_IfOtdrFiberSpanSubrack_Type())
ifOtdrFiberSpanSubrack.setMaxAccess(_F)
if mibBuilder.loadTexts:ifOtdrFiberSpanSubrack.setStatus(_A)
_IfOtdrFiberSpanSlot_Type=SlotNumber
_IfOtdrFiberSpanSlot_Object=MibTableColumn
ifOtdrFiberSpanSlot=_IfOtdrFiberSpanSlot_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,8),_IfOtdrFiberSpanSlot_Type())
ifOtdrFiberSpanSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:ifOtdrFiberSpanSlot.setStatus(_A)
_IfOtdrFiberSpanPortNr_Type=PortNumber
_IfOtdrFiberSpanPortNr_Object=MibTableColumn
ifOtdrFiberSpanPortNr=_IfOtdrFiberSpanPortNr_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,9),_IfOtdrFiberSpanPortNr_Type())
ifOtdrFiberSpanPortNr.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtdrFiberSpanPortNr.setStatus(_A)
class _IfOtdrFiberSpanState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('measuring',1)))
_IfOtdrFiberSpanState_Type.__name__=_D
_IfOtdrFiberSpanState_Object=MibTableColumn
ifOtdrFiberSpanState=_IfOtdrFiberSpanState_Object((1,3,6,1,4,1,8708,2,72,2,2,1,1,10),_IfOtdrFiberSpanState_Type())
ifOtdrFiberSpanState.setMaxAccess(_C)
if mibBuilder.loadTexts:ifOtdrFiberSpanState.setStatus(_A)
ifOtdrGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,72,1,1,1))
ifOtdrGeneralGroupV1.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ifOtdrGeneralGroupV1.setStatus(_A)
ifOtdrFiberSpanGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,72,1,1,2))
ifOtdrFiberSpanGroupV1.setObjects(*((_B,_E),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ifOtdrFiberSpanGroupV1.setStatus(_A)
lumIfOtdrComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,72,1,2,1))
lumIfOtdrComplV1.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:lumIfOtdrComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ifOtdrMIBModule':ifOtdrMIBModule,'lumIfOtdrConfs':lumIfOtdrConfs,'lumIfOtdrGroups':lumIfOtdrGroups,_T:ifOtdrGeneralGroupV1,_U:ifOtdrFiberSpanGroupV1,'lumIfOtdrCompl':lumIfOtdrCompl,'lumIfOtdrComplV1':lumIfOtdrComplV1,'lumIfOtdrMIBObjects':lumIfOtdrMIBObjects,'ifOtdrGeneral':ifOtdrGeneral,_I:ifOtdrGeneralConfigLastChangeTime,_J:ifOtdrGeneralStateLastChangeTime,'ifOtdrGeneralFiberSpanTableSize':ifOtdrGeneralFiberSpanTableSize,'ifOtdrFiberSpanList':ifOtdrFiberSpanList,'ifOtdrFiberSpanTable':ifOtdrFiberSpanTable,'ifOtdrFiberSpanEntry':ifOtdrFiberSpanEntry,_E:ifOtdrFiberSpanIndex,_K:ifOtdrFiberSpanName,_L:ifOtdrFiberSpanFiberId,_M:ifOtdrFiberSpanSessionType,_N:ifOtdrFiberSpanStartMeasurementCommand,_O:ifOtdrFiberSpanConnIfBasicIfIndex,_P:ifOtdrFiberSpanSubrack,_Q:ifOtdrFiberSpanSlot,_R:ifOtdrFiberSpanPortNr,_S:ifOtdrFiberSpanState})