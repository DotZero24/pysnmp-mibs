_Q='chCompMIBCompID'
_P='chCompMIBSlotID'
_O='chCompMIBID'
_N='chSlotCompID'
_M='chSlotID'
_L='chCompID'
_K='chBackplaneID'
_J='invalid'
_I='unknown'
_H='DisplayString'
_G='Integer32'
_F='OctetString'
_E='CT-CHASSIS-MIB'
_D='deprecated'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
chassis,=mibBuilder.importSymbols('CTRON-MIB-NAMES','chassis')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_ChType_Type=ObjectIdentifier
_ChType_Object=MibScalar
chType=_ChType_Object((1,3,6,1,4,1,52,4,1,1,2,1),_ChType_Type())
chType.setMaxAccess(_B)
if mibBuilder.loadTexts:chType.setStatus(_A)
_ChBackplaneTable_Object=MibTable
chBackplaneTable=_ChBackplaneTable_Object((1,3,6,1,4,1,52,4,1,1,2,2))
if mibBuilder.loadTexts:chBackplaneTable.setStatus(_A)
_ChBackplaneEntry_Object=MibTableRow
chBackplaneEntry=_ChBackplaneEntry_Object((1,3,6,1,4,1,52,4,1,1,2,2,1))
chBackplaneEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:chBackplaneEntry.setStatus(_A)
_ChBackplaneID_Type=Integer32
_ChBackplaneID_Object=MibTableColumn
chBackplaneID=_ChBackplaneID_Object((1,3,6,1,4,1,52,4,1,1,2,2,1,1),_ChBackplaneID_Type())
chBackplaneID.setMaxAccess(_B)
if mibBuilder.loadTexts:chBackplaneID.setStatus(_A)
_ChBackplaneType_Type=ObjectIdentifier
_ChBackplaneType_Object=MibTableColumn
chBackplaneType=_ChBackplaneType_Object((1,3,6,1,4,1,52,4,1,1,2,2,1,2),_ChBackplaneType_Type())
chBackplaneType.setMaxAccess(_B)
if mibBuilder.loadTexts:chBackplaneType.setStatus(_A)
class _ChNumSlots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ChNumSlots_Type.__name__=_G
_ChNumSlots_Object=MibScalar
chNumSlots=_ChNumSlots_Object((1,3,6,1,4,1,52,4,1,1,2,3),_ChNumSlots_Type())
chNumSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:chNumSlots.setStatus(_A)
_ChCompTable_Object=MibTable
chCompTable=_ChCompTable_Object((1,3,6,1,4,1,52,4,1,1,2,4))
if mibBuilder.loadTexts:chCompTable.setStatus(_A)
_ChCompEntry_Object=MibTableRow
chCompEntry=_ChCompEntry_Object((1,3,6,1,4,1,52,4,1,1,2,4,1))
chCompEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:chCompEntry.setStatus(_A)
_ChCompID_Type=Integer32
_ChCompID_Object=MibTableColumn
chCompID=_ChCompID_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,1),_ChCompID_Type())
chCompID.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompID.setStatus(_A)
class _ChCompAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_J,2),('enabled',3),('testing',4),('operational',5),('error',6),('disabled',7),('delete',8)))
_ChCompAdminStatus_Type.__name__=_G
_ChCompAdminStatus_Object=MibTableColumn
chCompAdminStatus=_ChCompAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,2),_ChCompAdminStatus_Type())
chCompAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompAdminStatus.setStatus(_A)
class _ChCompArg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_ChCompArg_Type.__name__=_F
_ChCompArg_Object=MibTableColumn
chCompArg=_ChCompArg_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,3),_ChCompArg_Type())
chCompArg.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompArg.setStatus(_A)
_ChCompType_Type=ObjectIdentifier
_ChCompType_Object=MibTableColumn
chCompType=_ChCompType_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,4),_ChCompType_Type())
chCompType.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompType.setStatus(_A)
class _ChCompName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChCompName_Type.__name__=_H
_ChCompName_Object=MibTableColumn
chCompName=_ChCompName_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,5),_ChCompName_Type())
chCompName.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompName.setStatus(_A)
class _ChCompVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChCompVersion_Type.__name__=_H
_ChCompVersion_Object=MibTableColumn
chCompVersion=_ChCompVersion_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,6),_ChCompVersion_Type())
chCompVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompVersion.setStatus(_A)
_ChCompTimeStamp_Type=TimeTicks
_ChCompTimeStamp_Object=MibTableColumn
chCompTimeStamp=_ChCompTimeStamp_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,7),_ChCompTimeStamp_Type())
chCompTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompTimeStamp.setStatus(_A)
class _ChCompAccessPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),('same',3),('otherCommStr',4),('other',5)))
_ChCompAccessPolicy_Type.__name__=_G
_ChCompAccessPolicy_Object=MibTableColumn
chCompAccessPolicy=_ChCompAccessPolicy_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,8),_ChCompAccessPolicy_Type())
chCompAccessPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompAccessPolicy.setStatus(_A)
_ChCompBasicCommStr_Type=OctetString
_ChCompBasicCommStr_Object=MibTableColumn
chCompBasicCommStr=_ChCompBasicCommStr_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,9),_ChCompBasicCommStr_Type())
chCompBasicCommStr.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompBasicCommStr.setStatus(_A)
_ChCompROCommStr_Type=OctetString
_ChCompROCommStr_Object=MibTableColumn
chCompROCommStr=_ChCompROCommStr_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,10),_ChCompROCommStr_Type())
chCompROCommStr.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompROCommStr.setStatus(_A)
_ChCompRWCommStr_Type=OctetString
_ChCompRWCommStr_Object=MibTableColumn
chCompRWCommStr=_ChCompRWCommStr_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,11),_ChCompRWCommStr_Type())
chCompRWCommStr.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompRWCommStr.setStatus(_A)
_ChCompSUCommStr_Type=OctetString
_ChCompSUCommStr_Object=MibTableColumn
chCompSUCommStr=_ChCompSUCommStr_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,12),_ChCompSUCommStr_Type())
chCompSUCommStr.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompSUCommStr.setStatus(_A)
_ChCompNetAdr_Type=IpAddress
_ChCompNetAdr_Object=MibTableColumn
chCompNetAdr=_ChCompNetAdr_Object((1,3,6,1,4,1,52,4,1,1,2,4,1,13),_ChCompNetAdr_Type())
chCompNetAdr.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompNetAdr.setStatus(_A)
_ChSlotTable_Object=MibTable
chSlotTable=_ChSlotTable_Object((1,3,6,1,4,1,52,4,1,1,2,5))
if mibBuilder.loadTexts:chSlotTable.setStatus(_A)
_ChSlotEntry_Object=MibTableRow
chSlotEntry=_ChSlotEntry_Object((1,3,6,1,4,1,52,4,1,1,2,5,1))
chSlotEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:chSlotEntry.setStatus(_A)
_ChSlotID_Type=Integer32
_ChSlotID_Object=MibTableColumn
chSlotID=_ChSlotID_Object((1,3,6,1,4,1,52,4,1,1,2,5,1,1),_ChSlotID_Type())
chSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:chSlotID.setStatus(_A)
_ChSlotCompID_Type=Integer32
_ChSlotCompID_Object=MibTableColumn
chSlotCompID=_ChSlotCompID_Object((1,3,6,1,4,1,52,4,1,1,2,5,1,2),_ChSlotCompID_Type())
chSlotCompID.setMaxAccess(_B)
if mibBuilder.loadTexts:chSlotCompID.setStatus(_A)
_ChSlotClass_Type=ObjectIdentifier
_ChSlotClass_Object=MibTableColumn
chSlotClass=_ChSlotClass_Object((1,3,6,1,4,1,52,4,1,1,2,5,1,3),_ChSlotClass_Type())
chSlotClass.setMaxAccess(_B)
if mibBuilder.loadTexts:chSlotClass.setStatus(_A)
_ChSlotModuleType_Type=ObjectIdentifier
_ChSlotModuleType_Object=MibTableColumn
chSlotModuleType=_ChSlotModuleType_Object((1,3,6,1,4,1,52,4,1,1,2,5,1,4),_ChSlotModuleType_Type())
chSlotModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:chSlotModuleType.setStatus(_A)
class _ChSlotModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChSlotModuleName_Type.__name__=_H
_ChSlotModuleName_Object=MibTableColumn
chSlotModuleName=_ChSlotModuleName_Object((1,3,6,1,4,1,52,4,1,1,2,5,1,5),_ChSlotModuleName_Type())
chSlotModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:chSlotModuleName.setStatus(_A)
class _ChSlotModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChSlotModuleVersion_Type.__name__=_H
_ChSlotModuleVersion_Object=MibTableColumn
chSlotModuleVersion=_ChSlotModuleVersion_Object((1,3,6,1,4,1,52,4,1,1,2,5,1,6),_ChSlotModuleVersion_Type())
chSlotModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chSlotModuleVersion.setStatus(_A)
_ChSlotModuleTimeStamp_Type=TimeTicks
_ChSlotModuleTimeStamp_Object=MibTableColumn
chSlotModuleTimeStamp=_ChSlotModuleTimeStamp_Object((1,3,6,1,4,1,52,4,1,1,2,5,1,7),_ChSlotModuleTimeStamp_Type())
chSlotModuleTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:chSlotModuleTimeStamp.setStatus(_A)
_ChCompMIBTable_Object=MibTable
chCompMIBTable=_ChCompMIBTable_Object((1,3,6,1,4,1,52,4,1,1,2,6))
if mibBuilder.loadTexts:chCompMIBTable.setStatus(_D)
_ChCompMIBEntry_Object=MibTableRow
chCompMIBEntry=_ChCompMIBEntry_Object((1,3,6,1,4,1,52,4,1,1,2,6,1))
chCompMIBEntry.setIndexNames((0,_E,_O),(0,_E,_P),(0,_E,_Q))
if mibBuilder.loadTexts:chCompMIBEntry.setStatus(_D)
_ChCompMIBID_Type=Integer32
_ChCompMIBID_Object=MibTableColumn
chCompMIBID=_ChCompMIBID_Object((1,3,6,1,4,1,52,4,1,1,2,6,1,1),_ChCompMIBID_Type())
chCompMIBID.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompMIBID.setStatus(_D)
_ChCompMIBSlotID_Type=Integer32
_ChCompMIBSlotID_Object=MibTableColumn
chCompMIBSlotID=_ChCompMIBSlotID_Object((1,3,6,1,4,1,52,4,1,1,2,6,1,2),_ChCompMIBSlotID_Type())
chCompMIBSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompMIBSlotID.setStatus(_D)
_ChCompMIBCompID_Type=Integer32
_ChCompMIBCompID_Object=MibTableColumn
chCompMIBCompID=_ChCompMIBCompID_Object((1,3,6,1,4,1,52,4,1,1,2,6,1,3),_ChCompMIBCompID_Type())
chCompMIBCompID.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompMIBCompID.setStatus(_D)
_ChCompMIBGrpOID_Type=ObjectIdentifier
_ChCompMIBGrpOID_Object=MibTableColumn
chCompMIBGrpOID=_ChCompMIBGrpOID_Object((1,3,6,1,4,1,52,4,1,1,2,6,1,4),_ChCompMIBGrpOID_Type())
chCompMIBGrpOID.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompMIBGrpOID.setStatus(_D)
_ChCompMIBVectorObjectBase_Type=ObjectIdentifier
_ChCompMIBVectorObjectBase_Object=MibTableColumn
chCompMIBVectorObjectBase=_ChCompMIBVectorObjectBase_Object((1,3,6,1,4,1,52,4,1,1,2,6,1,5),_ChCompMIBVectorObjectBase_Type())
chCompMIBVectorObjectBase.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompMIBVectorObjectBase.setStatus(_D)
_ChCompMIBVectorNum_Type=Integer32
_ChCompMIBVectorNum_Object=MibTableColumn
chCompMIBVectorNum=_ChCompMIBVectorNum_Object((1,3,6,1,4,1,52,4,1,1,2,6,1,6),_ChCompMIBVectorNum_Type())
chCompMIBVectorNum.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompMIBVectorNum.setStatus(_D)
class _ChCompMIBType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-instanced',1),('instanced',2)))
_ChCompMIBType_Type.__name__=_G
_ChCompMIBType_Object=MibTableColumn
chCompMIBType=_ChCompMIBType_Object((1,3,6,1,4,1,52,4,1,1,2,6,1,7),_ChCompMIBType_Type())
chCompMIBType.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompMIBType.setStatus(_D)
class _ChCompMIBStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),('agent',3),('management',4)))
_ChCompMIBStatus_Type.__name__=_G
_ChCompMIBStatus_Object=MibTableColumn
chCompMIBStatus=_ChCompMIBStatus_Object((1,3,6,1,4,1,52,4,1,1,2,6,1,8),_ChCompMIBStatus_Type())
chCompMIBStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chCompMIBStatus.setStatus(_D)
_ChPhysicalChanges_Type=Counter32
_ChPhysicalChanges_Object=MibScalar
chPhysicalChanges=_ChPhysicalChanges_Object((1,3,6,1,4,1,52,4,1,1,2,7),_ChPhysicalChanges_Type())
chPhysicalChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:chPhysicalChanges.setStatus(_D)
_ChLogicalChanges_Type=Counter32
_ChLogicalChanges_Object=MibScalar
chLogicalChanges=_ChLogicalChanges_Object((1,3,6,1,4,1,52,4,1,1,2,8),_ChLogicalChanges_Type())
chLogicalChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:chLogicalChanges.setStatus(_D)
class _ChCompGlobalBasicCommStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,27))
_ChCompGlobalBasicCommStr_Type.__name__=_F
_ChCompGlobalBasicCommStr_Object=MibScalar
chCompGlobalBasicCommStr=_ChCompGlobalBasicCommStr_Object((1,3,6,1,4,1,52,4,1,1,2,9),_ChCompGlobalBasicCommStr_Type())
chCompGlobalBasicCommStr.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompGlobalBasicCommStr.setStatus(_A)
class _ChCompGlobalROCommStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,27))
_ChCompGlobalROCommStr_Type.__name__=_F
_ChCompGlobalROCommStr_Object=MibScalar
chCompGlobalROCommStr=_ChCompGlobalROCommStr_Object((1,3,6,1,4,1,52,4,1,1,2,10),_ChCompGlobalROCommStr_Type())
chCompGlobalROCommStr.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompGlobalROCommStr.setStatus(_A)
class _ChCompGlobalRWCommStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,27))
_ChCompGlobalRWCommStr_Type.__name__=_F
_ChCompGlobalRWCommStr_Object=MibScalar
chCompGlobalRWCommStr=_ChCompGlobalRWCommStr_Object((1,3,6,1,4,1,52,4,1,1,2,11),_ChCompGlobalRWCommStr_Type())
chCompGlobalRWCommStr.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompGlobalRWCommStr.setStatus(_A)
class _ChCompGlobalSUCommStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,27))
_ChCompGlobalSUCommStr_Type.__name__=_F
_ChCompGlobalSUCommStr_Object=MibScalar
chCompGlobalSUCommStr=_ChCompGlobalSUCommStr_Object((1,3,6,1,4,1,52,4,1,1,2,12),_ChCompGlobalSUCommStr_Type())
chCompGlobalSUCommStr.setMaxAccess(_C)
if mibBuilder.loadTexts:chCompGlobalSUCommStr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'chType':chType,'chBackplaneTable':chBackplaneTable,'chBackplaneEntry':chBackplaneEntry,_K:chBackplaneID,'chBackplaneType':chBackplaneType,'chNumSlots':chNumSlots,'chCompTable':chCompTable,'chCompEntry':chCompEntry,_L:chCompID,'chCompAdminStatus':chCompAdminStatus,'chCompArg':chCompArg,'chCompType':chCompType,'chCompName':chCompName,'chCompVersion':chCompVersion,'chCompTimeStamp':chCompTimeStamp,'chCompAccessPolicy':chCompAccessPolicy,'chCompBasicCommStr':chCompBasicCommStr,'chCompROCommStr':chCompROCommStr,'chCompRWCommStr':chCompRWCommStr,'chCompSUCommStr':chCompSUCommStr,'chCompNetAdr':chCompNetAdr,'chSlotTable':chSlotTable,'chSlotEntry':chSlotEntry,_M:chSlotID,_N:chSlotCompID,'chSlotClass':chSlotClass,'chSlotModuleType':chSlotModuleType,'chSlotModuleName':chSlotModuleName,'chSlotModuleVersion':chSlotModuleVersion,'chSlotModuleTimeStamp':chSlotModuleTimeStamp,'chCompMIBTable':chCompMIBTable,'chCompMIBEntry':chCompMIBEntry,_O:chCompMIBID,_P:chCompMIBSlotID,_Q:chCompMIBCompID,'chCompMIBGrpOID':chCompMIBGrpOID,'chCompMIBVectorObjectBase':chCompMIBVectorObjectBase,'chCompMIBVectorNum':chCompMIBVectorNum,'chCompMIBType':chCompMIBType,'chCompMIBStatus':chCompMIBStatus,'chPhysicalChanges':chPhysicalChanges,'chLogicalChanges':chLogicalChanges,'chCompGlobalBasicCommStr':chCompGlobalBasicCommStr,'chCompGlobalROCommStr':chCompGlobalROCommStr,'chCompGlobalRWCommStr':chCompGlobalRWCommStr,'chCompGlobalSUCommStr':chCompGlobalSUCommStr})