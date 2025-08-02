_a='mclagGroupV1'
_Z='mclagInternalReference'
_Y='mclagProtectionStateDegraded'
_X='mclagProtectionStateFailure'
_W='mclagLagStatus'
_V='mclagLagOperPortPrio'
_U='mclagLagAdminPortPrio'
_T='mclagLagOperSystemPrio'
_S='mclagLagAdminSystemPrio'
_R='mclagControlledLag'
_Q='mclagSynchronizationStatus'
_P='mclagRgId'
_O='mclagNodeId'
_N='mclagDescr'
_M='mclagName'
_L='mclagGeneralMclagTableSize'
_K='mclagGeneralStateLastChangeTime'
_J='mclagGeneralLastChangeTime'
_I='mclagIndex'
_H='DisplayString'
_G='Integer32'
_F='read-write'
_E='read-create'
_D='read-only'
_C='Unsigned32'
_B='LUM-MCLAG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumMclagMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumMclagMIB','lumModules')
FaultStatus,MgmtNameString=mibBuilder.importSymbols('LUM-TC','FaultStatus','MgmtNameString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'PhysAddress','TextualConvention')
lumMclagMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,62))
if mibBuilder.loadTexts:lumMclagMIBModule.setRevisions(('2017-06-15 00:00','2015-01-14 00:00','2014-11-05 00:00'))
class MclagLabel(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
class MclagIdentifier(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LumMclagConfs_ObjectIdentity=ObjectIdentity
lumMclagConfs=_LumMclagConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,62,1))
_LumMclagGroups_ObjectIdentity=ObjectIdentity
lumMclagGroups=_LumMclagGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,62,1,1))
_LumMclagCompl_ObjectIdentity=ObjectIdentity
lumMclagCompl=_LumMclagCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,62,1,2))
_LumMclagMIBObjects_ObjectIdentity=ObjectIdentity
lumMclagMIBObjects=_LumMclagMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,62,2))
_MclagGeneral_ObjectIdentity=ObjectIdentity
mclagGeneral=_MclagGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,62,2,1))
_MclagGeneralLastChangeTime_Type=DateAndTime
_MclagGeneralLastChangeTime_Object=MibScalar
mclagGeneralLastChangeTime=_MclagGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,62,2,1,1),_MclagGeneralLastChangeTime_Type())
mclagGeneralLastChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mclagGeneralLastChangeTime.setStatus(_A)
_MclagGeneralStateLastChangeTime_Type=DateAndTime
_MclagGeneralStateLastChangeTime_Object=MibScalar
mclagGeneralStateLastChangeTime=_MclagGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,62,2,1,2),_MclagGeneralStateLastChangeTime_Type())
mclagGeneralStateLastChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mclagGeneralStateLastChangeTime.setStatus(_A)
_MclagGeneralMclagTableSize_Type=Unsigned32
_MclagGeneralMclagTableSize_Object=MibScalar
mclagGeneralMclagTableSize=_MclagGeneralMclagTableSize_Object((1,3,6,1,4,1,8708,2,62,2,1,3),_MclagGeneralMclagTableSize_Type())
mclagGeneralMclagTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:mclagGeneralMclagTableSize.setStatus(_A)
_MclagList_ObjectIdentity=ObjectIdentity
mclagList=_MclagList_ObjectIdentity((1,3,6,1,4,1,8708,2,62,2,2))
_MclagTable_Object=MibTable
mclagTable=_MclagTable_Object((1,3,6,1,4,1,8708,2,62,2,2,1))
if mibBuilder.loadTexts:mclagTable.setStatus(_A)
_MclagEntry_Object=MibTableRow
mclagEntry=_MclagEntry_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1))
mclagEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:mclagEntry.setStatus(_A)
class _MclagIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MclagIndex_Type.__name__=_C
_MclagIndex_Object=MibTableColumn
mclagIndex=_MclagIndex_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,1),_MclagIndex_Type())
mclagIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mclagIndex.setStatus(_A)
_MclagName_Type=MgmtNameString
_MclagName_Object=MibTableColumn
mclagName=_MclagName_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,2),_MclagName_Type())
mclagName.setMaxAccess(_D)
if mibBuilder.loadTexts:mclagName.setStatus(_A)
class _MclagDescr_Type(DisplayString):defaultValue=OctetString('')
_MclagDescr_Type.__name__=_H
_MclagDescr_Object=MibTableColumn
mclagDescr=_MclagDescr_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,3),_MclagDescr_Type())
mclagDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:mclagDescr.setStatus(_A)
class _MclagNodeId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MclagNodeId_Type.__name__=_C
_MclagNodeId_Object=MibTableColumn
mclagNodeId=_MclagNodeId_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,4),_MclagNodeId_Type())
mclagNodeId.setMaxAccess(_F)
if mibBuilder.loadTexts:mclagNodeId.setStatus(_A)
class _MclagRgId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_MclagRgId_Type.__name__=_C
_MclagRgId_Object=MibTableColumn
mclagRgId=_MclagRgId_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,5),_MclagRgId_Type())
mclagRgId.setMaxAccess(_F)
if mibBuilder.loadTexts:mclagRgId.setStatus(_A)
class _MclagSynchronizationStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unSynchronized',1),('synchronized',2),('undefined',3)))
_MclagSynchronizationStatus_Type.__name__=_G
_MclagSynchronizationStatus_Object=MibTableColumn
mclagSynchronizationStatus=_MclagSynchronizationStatus_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,6),_MclagSynchronizationStatus_Type())
mclagSynchronizationStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mclagSynchronizationStatus.setStatus(_A)
class _MclagControlledLag_Type(DisplayString):defaultValue=OctetString('')
_MclagControlledLag_Type.__name__=_H
_MclagControlledLag_Object=MibTableColumn
mclagControlledLag=_MclagControlledLag_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,7),_MclagControlledLag_Type())
mclagControlledLag.setMaxAccess(_F)
if mibBuilder.loadTexts:mclagControlledLag.setStatus(_A)
class _MclagLagAdminSystemPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MclagLagAdminSystemPrio_Type.__name__=_C
_MclagLagAdminSystemPrio_Object=MibTableColumn
mclagLagAdminSystemPrio=_MclagLagAdminSystemPrio_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,8),_MclagLagAdminSystemPrio_Type())
mclagLagAdminSystemPrio.setMaxAccess(_E)
if mibBuilder.loadTexts:mclagLagAdminSystemPrio.setStatus(_A)
class _MclagLagOperSystemPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MclagLagOperSystemPrio_Type.__name__=_C
_MclagLagOperSystemPrio_Object=MibTableColumn
mclagLagOperSystemPrio=_MclagLagOperSystemPrio_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,9),_MclagLagOperSystemPrio_Type())
mclagLagOperSystemPrio.setMaxAccess(_E)
if mibBuilder.loadTexts:mclagLagOperSystemPrio.setStatus(_A)
class _MclagLagAdminPortPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MclagLagAdminPortPrio_Type.__name__=_C
_MclagLagAdminPortPrio_Object=MibTableColumn
mclagLagAdminPortPrio=_MclagLagAdminPortPrio_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,10),_MclagLagAdminPortPrio_Type())
mclagLagAdminPortPrio.setMaxAccess(_E)
if mibBuilder.loadTexts:mclagLagAdminPortPrio.setStatus(_A)
class _MclagLagOperPortPrio_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MclagLagOperPortPrio_Type.__name__=_C
_MclagLagOperPortPrio_Object=MibTableColumn
mclagLagOperPortPrio=_MclagLagOperPortPrio_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,11),_MclagLagOperPortPrio_Type())
mclagLagOperPortPrio.setMaxAccess(_E)
if mibBuilder.loadTexts:mclagLagOperPortPrio.setStatus(_A)
class _MclagLagStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standby',1),('active',2)))
_MclagLagStatus_Type.__name__=_G
_MclagLagStatus_Object=MibTableColumn
mclagLagStatus=_MclagLagStatus_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,12),_MclagLagStatus_Type())
mclagLagStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mclagLagStatus.setStatus(_A)
_MclagProtectionStateFailure_Type=FaultStatus
_MclagProtectionStateFailure_Object=MibTableColumn
mclagProtectionStateFailure=_MclagProtectionStateFailure_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,13),_MclagProtectionStateFailure_Type())
mclagProtectionStateFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:mclagProtectionStateFailure.setStatus(_A)
_MclagProtectionStateDegraded_Type=FaultStatus
_MclagProtectionStateDegraded_Object=MibTableColumn
mclagProtectionStateDegraded=_MclagProtectionStateDegraded_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,14),_MclagProtectionStateDegraded_Type())
mclagProtectionStateDegraded.setMaxAccess(_D)
if mibBuilder.loadTexts:mclagProtectionStateDegraded.setStatus(_A)
class _MclagInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MclagInternalReference_Type.__name__=_C
_MclagInternalReference_Object=MibTableColumn
mclagInternalReference=_MclagInternalReference_Object((1,3,6,1,4,1,8708,2,62,2,2,1,1,15),_MclagInternalReference_Type())
mclagInternalReference.setMaxAccess(_E)
if mibBuilder.loadTexts:mclagInternalReference.setStatus(_A)
mclagGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,62,1,1,1))
mclagGeneralGroupV1.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:mclagGeneralGroupV1.setStatus(_A)
mclagGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,62,1,1,2))
mclagGroupV1.setObjects(*((_B,_I),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:mclagGroupV1.setStatus(_A)
lumMclagBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,62,1,2,1))
lumMclagBasicComplV1.setObjects((_B,_a))
if mibBuilder.loadTexts:lumMclagBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MclagLabel':MclagLabel,'MclagIdentifier':MclagIdentifier,'lumMclagMIBModule':lumMclagMIBModule,'lumMclagConfs':lumMclagConfs,'lumMclagGroups':lumMclagGroups,'mclagGeneralGroupV1':mclagGeneralGroupV1,_a:mclagGroupV1,'lumMclagCompl':lumMclagCompl,'lumMclagBasicComplV1':lumMclagBasicComplV1,'lumMclagMIBObjects':lumMclagMIBObjects,'mclagGeneral':mclagGeneral,_J:mclagGeneralLastChangeTime,_K:mclagGeneralStateLastChangeTime,_L:mclagGeneralMclagTableSize,'mclagList':mclagList,'mclagTable':mclagTable,'mclagEntry':mclagEntry,_I:mclagIndex,_M:mclagName,_N:mclagDescr,_O:mclagNodeId,_P:mclagRgId,_Q:mclagSynchronizationStatus,_R:mclagControlledLag,_S:mclagLagAdminSystemPrio,_T:mclagLagOperSystemPrio,_U:mclagLagAdminPortPrio,_V:mclagLagOperPortPrio,_W:mclagLagStatus,_X:mclagProtectionStateFailure,_Y:mclagProtectionStateDegraded,_Z:mclagInternalReference})