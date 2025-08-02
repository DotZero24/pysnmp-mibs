_k='cpqCrSpareScsiID'
_j='cpqCrPartitionIndex'
_i='cpqCrPartitionLogDrvIndex'
_h='formatting'
_g='addingSpare'
_f='rebuilding'
_e='creating'
_d='warmSpare'
_c='hotSpare'
_b='online'
_a='offline'
_Z='cpqCrSparePhyDrvIndex'
_Y='cpqCrSpareCntlrIndex'
_X='initializing'
_W='reconstructing'
_V='reduced'
_U='raid0plus1'
_T='cpqCrLogDrvCntlrIndex'
_S='cpqCrCntlrIndex'
_R='NotificationType'
_Q='deprecated'
_P='cpqCrPhyDrvCntlrIndex'
_O='OctetString'
_N='cpqCrPhyDrvScsiID'
_M='DisplayString'
_L='cpqCrPhyDrvIndex'
_K='cpqCrLogDrvIndex'
_J='degraded'
_I='ok'
_H='failed'
_G='CPQCR-MIB'
_F='other'
_E='sysName'
_D='SNMPv2-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols('CPQHOST-MIB','compaq','cpqHoTrapFlags')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_D,_E)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_R,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_R,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention')
_CpqClusteredRAID_ObjectIdentity=ObjectIdentity
cpqClusteredRAID=_CpqClusteredRAID_ObjectIdentity((1,3,6,1,4,1,232,141))
_CpqCrMibRev_ObjectIdentity=ObjectIdentity
cpqCrMibRev=_CpqCrMibRev_ObjectIdentity((1,3,6,1,4,1,232,141,1))
class _CpqCrMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqCrMibRevMajor_Type.__name__=_C
_CpqCrMibRevMajor_Object=MibScalar
cpqCrMibRevMajor=_CpqCrMibRevMajor_Object((1,3,6,1,4,1,232,141,1,1),_CpqCrMibRevMajor_Type())
cpqCrMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrMibRevMajor.setStatus(_A)
class _CpqCrMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqCrMibRevMinor_Type.__name__=_C
_CpqCrMibRevMinor_Object=MibScalar
cpqCrMibRevMinor=_CpqCrMibRevMinor_Object((1,3,6,1,4,1,232,141,1,2),_CpqCrMibRevMinor_Type())
cpqCrMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrMibRevMinor.setStatus(_A)
class _CpqCrMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrMibCondition_Type.__name__=_C
_CpqCrMibCondition_Object=MibScalar
cpqCrMibCondition=_CpqCrMibCondition_Object((1,3,6,1,4,1,232,141,1,3),_CpqCrMibCondition_Type())
cpqCrMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrMibCondition.setStatus(_A)
_CpqCrComponent_ObjectIdentity=ObjectIdentity
cpqCrComponent=_CpqCrComponent_ObjectIdentity((1,3,6,1,4,1,232,141,2))
_CpqCrInterface_ObjectIdentity=ObjectIdentity
cpqCrInterface=_CpqCrInterface_ObjectIdentity((1,3,6,1,4,1,232,141,2,1))
_CpqCrOsCommon_ObjectIdentity=ObjectIdentity
cpqCrOsCommon=_CpqCrOsCommon_ObjectIdentity((1,3,6,1,4,1,232,141,2,1,4))
class _CpqCrOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqCrOsCommonPollFreq_Type.__name__=_C
_CpqCrOsCommonPollFreq_Object=MibScalar
cpqCrOsCommonPollFreq=_CpqCrOsCommonPollFreq_Object((1,3,6,1,4,1,232,141,2,1,4,1),_CpqCrOsCommonPollFreq_Type())
cpqCrOsCommonPollFreq.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqCrOsCommonPollFreq.setStatus(_A)
_CpqCrCntlr_ObjectIdentity=ObjectIdentity
cpqCrCntlr=_CpqCrCntlr_ObjectIdentity((1,3,6,1,4,1,232,141,2,2))
_CpqCrCntlrTable_Object=MibTable
cpqCrCntlrTable=_CpqCrCntlrTable_Object((1,3,6,1,4,1,232,141,2,2,1))
if mibBuilder.loadTexts:cpqCrCntlrTable.setStatus(_A)
_CpqCrCntlrEntry_Object=MibTableRow
cpqCrCntlrEntry=_CpqCrCntlrEntry_Object((1,3,6,1,4,1,232,141,2,2,1,1))
cpqCrCntlrEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:cpqCrCntlrEntry.setStatus(_A)
class _CpqCrCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrCntlrIndex_Type.__name__=_C
_CpqCrCntlrIndex_Object=MibTableColumn
cpqCrCntlrIndex=_CpqCrCntlrIndex_Object((1,3,6,1,4,1,232,141,2,2,1,1,1),_CpqCrCntlrIndex_Type())
cpqCrCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrIndex.setStatus(_A)
class _CpqCrCntlrSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqCrCntlrSerialNumber_Type.__name__=_M
_CpqCrCntlrSerialNumber_Object=MibTableColumn
cpqCrCntlrSerialNumber=_CpqCrCntlrSerialNumber_Object((1,3,6,1,4,1,232,141,2,2,1,1,2),_CpqCrCntlrSerialNumber_Type())
cpqCrCntlrSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrSerialNumber.setStatus(_A)
class _CpqCrCntlrFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqCrCntlrFWRev_Type.__name__=_M
_CpqCrCntlrFWRev_Object=MibTableColumn
cpqCrCntlrFWRev=_CpqCrCntlrFWRev_Object((1,3,6,1,4,1,232,141,2,2,1,1,3),_CpqCrCntlrFWRev_Type())
cpqCrCntlrFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrFWRev.setStatus(_A)
class _CpqCrCntlrCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrCntlrCondition_Type.__name__=_C
_CpqCrCntlrCondition_Object=MibTableColumn
cpqCrCntlrCondition=_CpqCrCntlrCondition_Object((1,3,6,1,4,1,232,141,2,2,1,1,4),_CpqCrCntlrCondition_Type())
cpqCrCntlrCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrCondition.setStatus(_A)
class _CpqCrCntlrCurrentRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('notDuplexed',2),('active',3),('backup',4)))
_CpqCrCntlrCurrentRole_Type.__name__=_C
_CpqCrCntlrCurrentRole_Object=MibTableColumn
cpqCrCntlrCurrentRole=_CpqCrCntlrCurrentRole_Object((1,3,6,1,4,1,232,141,2,2,1,1,8),_CpqCrCntlrCurrentRole_Type())
cpqCrCntlrCurrentRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrCurrentRole.setStatus(_A)
class _CpqCrCntlrDriveOwnership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('owner',2),('notOwner',3)))
_CpqCrCntlrDriveOwnership_Type.__name__=_C
_CpqCrCntlrDriveOwnership_Object=MibTableColumn
cpqCrCntlrDriveOwnership=_CpqCrCntlrDriveOwnership_Object((1,3,6,1,4,1,232,141,2,2,1,1,9),_CpqCrCntlrDriveOwnership_Type())
cpqCrCntlrDriveOwnership.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrDriveOwnership.setStatus(_A)
class _CpqCrCntlrRebuildRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CpqCrCntlrRebuildRate_Type.__name__=_C
_CpqCrCntlrRebuildRate_Object=MibTableColumn
cpqCrCntlrRebuildRate=_CpqCrCntlrRebuildRate_Object((1,3,6,1,4,1,232,141,2,2,1,1,10),_CpqCrCntlrRebuildRate_Type())
cpqCrCntlrRebuildRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrRebuildRate.setStatus(_A)
class _CpqCrCntlrCreateRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CpqCrCntlrCreateRate_Type.__name__=_C
_CpqCrCntlrCreateRate_Object=MibTableColumn
cpqCrCntlrCreateRate=_CpqCrCntlrCreateRate_Object((1,3,6,1,4,1,232,141,2,2,1,1,11),_CpqCrCntlrCreateRate_Type())
cpqCrCntlrCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrCreateRate.setStatus(_A)
class _CpqCrCntlrCacheSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_CpqCrCntlrCacheSize_Type.__name__=_C
_CpqCrCntlrCacheSize_Object=MibTableColumn
cpqCrCntlrCacheSize=_CpqCrCntlrCacheSize_Object((1,3,6,1,4,1,232,141,2,2,1,1,12),_CpqCrCntlrCacheSize_Type())
cpqCrCntlrCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrCacheSize.setStatus(_A)
class _CpqCrCntlrSimmSizeA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_CpqCrCntlrSimmSizeA_Type.__name__=_C
_CpqCrCntlrSimmSizeA_Object=MibTableColumn
cpqCrCntlrSimmSizeA=_CpqCrCntlrSimmSizeA_Object((1,3,6,1,4,1,232,141,2,2,1,1,13),_CpqCrCntlrSimmSizeA_Type())
cpqCrCntlrSimmSizeA.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrSimmSizeA.setStatus(_A)
class _CpqCrCntlrSimmSizeB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_CpqCrCntlrSimmSizeB_Type.__name__=_C
_CpqCrCntlrSimmSizeB_Object=MibTableColumn
cpqCrCntlrSimmSizeB=_CpqCrCntlrSimmSizeB_Object((1,3,6,1,4,1,232,141,2,2,1,1,14),_CpqCrCntlrSimmSizeB_Type())
cpqCrCntlrSimmSizeB.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrCntlrSimmSizeB.setStatus(_A)
_CpqCrLogDrv_ObjectIdentity=ObjectIdentity
cpqCrLogDrv=_CpqCrLogDrv_ObjectIdentity((1,3,6,1,4,1,232,141,2,3))
_CpqCrLogDrvTable_Object=MibTable
cpqCrLogDrvTable=_CpqCrLogDrvTable_Object((1,3,6,1,4,1,232,141,2,3,1))
if mibBuilder.loadTexts:cpqCrLogDrvTable.setStatus(_A)
_CpqCrLogDrvEntry_Object=MibTableRow
cpqCrLogDrvEntry=_CpqCrLogDrvEntry_Object((1,3,6,1,4,1,232,141,2,3,1,1))
cpqCrLogDrvEntry.setIndexNames((0,_G,_T),(0,_G,_K))
if mibBuilder.loadTexts:cpqCrLogDrvEntry.setStatus(_A)
class _CpqCrLogDrvCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrLogDrvCntlrIndex_Type.__name__=_C
_CpqCrLogDrvCntlrIndex_Object=MibTableColumn
cpqCrLogDrvCntlrIndex=_CpqCrLogDrvCntlrIndex_Object((1,3,6,1,4,1,232,141,2,3,1,1,1),_CpqCrLogDrvCntlrIndex_Type())
cpqCrLogDrvCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvCntlrIndex.setStatus(_A)
class _CpqCrLogDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrLogDrvIndex_Type.__name__=_C
_CpqCrLogDrvIndex_Object=MibTableColumn
cpqCrLogDrvIndex=_CpqCrLogDrvIndex_Object((1,3,6,1,4,1,232,141,2,3,1,1,2),_CpqCrLogDrvIndex_Type())
cpqCrLogDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvIndex.setStatus(_A)
class _CpqCrLogDrvRAIDLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('jbod',2),('raid0',3),('raid1',4),(_U,5),('raid4',6),('raid5',7)))
_CpqCrLogDrvRAIDLevel_Type.__name__=_C
_CpqCrLogDrvRAIDLevel_Object=MibTableColumn
cpqCrLogDrvRAIDLevel=_CpqCrLogDrvRAIDLevel_Object((1,3,6,1,4,1,232,141,2,3,1,1,3),_CpqCrLogDrvRAIDLevel_Type())
cpqCrLogDrvRAIDLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvRAIDLevel.setStatus(_A)
class _CpqCrLogDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('good',2),(_V,3),(_H,4),(_W,5),(_X,6)))
_CpqCrLogDrvStatus_Type.__name__=_C
_CpqCrLogDrvStatus_Object=MibTableColumn
cpqCrLogDrvStatus=_CpqCrLogDrvStatus_Object((1,3,6,1,4,1,232,141,2,3,1,1,4),_CpqCrLogDrvStatus_Type())
cpqCrLogDrvStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvStatus.setStatus(_A)
class _CpqCrLogDrvRebuildPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpqCrLogDrvRebuildPercentage_Type.__name__=_C
_CpqCrLogDrvRebuildPercentage_Object=MibTableColumn
cpqCrLogDrvRebuildPercentage=_CpqCrLogDrvRebuildPercentage_Object((1,3,6,1,4,1,232,141,2,3,1,1,5),_CpqCrLogDrvRebuildPercentage_Type())
cpqCrLogDrvRebuildPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvRebuildPercentage.setStatus(_A)
class _CpqCrLogDrvAvailSpares_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqCrLogDrvAvailSpares_Type.__name__=_O
_CpqCrLogDrvAvailSpares_Object=MibTableColumn
cpqCrLogDrvAvailSpares=_CpqCrLogDrvAvailSpares_Object((1,3,6,1,4,1,232,141,2,3,1,1,7),_CpqCrLogDrvAvailSpares_Type())
cpqCrLogDrvAvailSpares.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvAvailSpares.setStatus(_A)
class _CpqCrLogDrvSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqCrLogDrvSize_Type.__name__=_C
_CpqCrLogDrvSize_Object=MibTableColumn
cpqCrLogDrvSize=_CpqCrLogDrvSize_Object((1,3,6,1,4,1,232,141,2,3,1,1,8),_CpqCrLogDrvSize_Type())
cpqCrLogDrvSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvSize.setStatus(_A)
class _CpqCrLogDrvPhyDrvIDs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqCrLogDrvPhyDrvIDs_Type.__name__=_O
_CpqCrLogDrvPhyDrvIDs_Object=MibTableColumn
cpqCrLogDrvPhyDrvIDs=_CpqCrLogDrvPhyDrvIDs_Object((1,3,6,1,4,1,232,141,2,3,1,1,9),_CpqCrLogDrvPhyDrvIDs_Type())
cpqCrLogDrvPhyDrvIDs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvPhyDrvIDs.setStatus(_A)
class _CpqCrLogDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrLogDrvCondition_Type.__name__=_C
_CpqCrLogDrvCondition_Object=MibTableColumn
cpqCrLogDrvCondition=_CpqCrLogDrvCondition_Object((1,3,6,1,4,1,232,141,2,3,1,1,10),_CpqCrLogDrvCondition_Type())
cpqCrLogDrvCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvCondition.setStatus(_A)
class _CpqCrLogDrvPartitionIDs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqCrLogDrvPartitionIDs_Type.__name__=_O
_CpqCrLogDrvPartitionIDs_Object=MibTableColumn
cpqCrLogDrvPartitionIDs=_CpqCrLogDrvPartitionIDs_Object((1,3,6,1,4,1,232,141,2,3,1,1,11),_CpqCrLogDrvPartitionIDs_Type())
cpqCrLogDrvPartitionIDs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrLogDrvPartitionIDs.setStatus(_A)
_CpqCrSpareDrv_ObjectIdentity=ObjectIdentity
cpqCrSpareDrv=_CpqCrSpareDrv_ObjectIdentity((1,3,6,1,4,1,232,141,2,4))
_CpqCrSpareTable_Object=MibTable
cpqCrSpareTable=_CpqCrSpareTable_Object((1,3,6,1,4,1,232,141,2,4,1))
if mibBuilder.loadTexts:cpqCrSpareTable.setStatus(_A)
_CpqCrSpareEntry_Object=MibTableRow
cpqCrSpareEntry=_CpqCrSpareEntry_Object((1,3,6,1,4,1,232,141,2,4,1,1))
cpqCrSpareEntry.setIndexNames((0,_G,_Y),(0,_G,_Z))
if mibBuilder.loadTexts:cpqCrSpareEntry.setStatus(_A)
class _CpqCrSpareCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrSpareCntlrIndex_Type.__name__=_C
_CpqCrSpareCntlrIndex_Object=MibTableColumn
cpqCrSpareCntlrIndex=_CpqCrSpareCntlrIndex_Object((1,3,6,1,4,1,232,141,2,4,1,1,1),_CpqCrSpareCntlrIndex_Type())
cpqCrSpareCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrSpareCntlrIndex.setStatus(_A)
class _CpqCrSparePhyDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrSparePhyDrvIndex_Type.__name__=_C
_CpqCrSparePhyDrvIndex_Object=MibTableColumn
cpqCrSparePhyDrvIndex=_CpqCrSparePhyDrvIndex_Object((1,3,6,1,4,1,232,141,2,4,1,1,2),_CpqCrSparePhyDrvIndex_Type())
cpqCrSparePhyDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrSparePhyDrvIndex.setStatus(_A)
class _CpqCrSpareStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),('empty',2),(_a,3),(_b,4),(_c,5),(_d,6),(_e,7),(_f,8),(_g,9),(_h,10)))
_CpqCrSpareStatus_Type.__name__=_C
_CpqCrSpareStatus_Object=MibTableColumn
cpqCrSpareStatus=_CpqCrSpareStatus_Object((1,3,6,1,4,1,232,141,2,4,1,1,3),_CpqCrSpareStatus_Type())
cpqCrSpareStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrSpareStatus.setStatus(_A)
class _CpqCrSpareCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrSpareCondition_Type.__name__=_C
_CpqCrSpareCondition_Object=MibTableColumn
cpqCrSpareCondition=_CpqCrSpareCondition_Object((1,3,6,1,4,1,232,141,2,4,1,1,4),_CpqCrSpareCondition_Type())
cpqCrSpareCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrSpareCondition.setStatus(_A)
class _CpqCrSpareScsiID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrSpareScsiID_Type.__name__=_C
_CpqCrSpareScsiID_Object=MibTableColumn
cpqCrSpareScsiID=_CpqCrSpareScsiID_Object((1,3,6,1,4,1,232,141,2,4,1,1,5),_CpqCrSpareScsiID_Type())
cpqCrSpareScsiID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrSpareScsiID.setStatus(_A)
_CpqCrPhyDrv_ObjectIdentity=ObjectIdentity
cpqCrPhyDrv=_CpqCrPhyDrv_ObjectIdentity((1,3,6,1,4,1,232,141,2,5))
_CpqCrPhyDrvTable_Object=MibTable
cpqCrPhyDrvTable=_CpqCrPhyDrvTable_Object((1,3,6,1,4,1,232,141,2,5,1))
if mibBuilder.loadTexts:cpqCrPhyDrvTable.setStatus(_A)
_CpqCrPhyDrvEntry_Object=MibTableRow
cpqCrPhyDrvEntry=_CpqCrPhyDrvEntry_Object((1,3,6,1,4,1,232,141,2,5,1,1))
cpqCrPhyDrvEntry.setIndexNames((0,_G,_P),(0,_G,_L))
if mibBuilder.loadTexts:cpqCrPhyDrvEntry.setStatus(_A)
class _CpqCrPhyDrvCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrPhyDrvCntlrIndex_Type.__name__=_C
_CpqCrPhyDrvCntlrIndex_Object=MibTableColumn
cpqCrPhyDrvCntlrIndex=_CpqCrPhyDrvCntlrIndex_Object((1,3,6,1,4,1,232,141,2,5,1,1,1),_CpqCrPhyDrvCntlrIndex_Type())
cpqCrPhyDrvCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvCntlrIndex.setStatus(_A)
class _CpqCrPhyDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrPhyDrvIndex_Type.__name__=_C
_CpqCrPhyDrvIndex_Object=MibTableColumn
cpqCrPhyDrvIndex=_CpqCrPhyDrvIndex_Object((1,3,6,1,4,1,232,141,2,5,1,1,2),_CpqCrPhyDrvIndex_Type())
cpqCrPhyDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvIndex.setStatus(_A)
class _CpqCrPhyDrvVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqCrPhyDrvVendor_Type.__name__=_M
_CpqCrPhyDrvVendor_Object=MibTableColumn
cpqCrPhyDrvVendor=_CpqCrPhyDrvVendor_Object((1,3,6,1,4,1,232,141,2,5,1,1,3),_CpqCrPhyDrvVendor_Type())
cpqCrPhyDrvVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvVendor.setStatus(_A)
class _CpqCrPhyDrvModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqCrPhyDrvModel_Type.__name__=_M
_CpqCrPhyDrvModel_Object=MibTableColumn
cpqCrPhyDrvModel=_CpqCrPhyDrvModel_Object((1,3,6,1,4,1,232,141,2,5,1,1,4),_CpqCrPhyDrvModel_Type())
cpqCrPhyDrvModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvModel.setStatus(_A)
class _CpqCrPhyDrvRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CpqCrPhyDrvRevision_Type.__name__=_M
_CpqCrPhyDrvRevision_Object=MibTableColumn
cpqCrPhyDrvRevision=_CpqCrPhyDrvRevision_Object((1,3,6,1,4,1,232,141,2,5,1,1,5),_CpqCrPhyDrvRevision_Type())
cpqCrPhyDrvRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvRevision.setStatus(_A)
class _CpqCrPhyDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),('empty',2),(_a,3),(_b,4),(_c,5),(_d,6),(_e,7),(_f,8),(_g,9),(_h,10)))
_CpqCrPhyDrvStatus_Type.__name__=_C
_CpqCrPhyDrvStatus_Object=MibTableColumn
cpqCrPhyDrvStatus=_CpqCrPhyDrvStatus_Object((1,3,6,1,4,1,232,141,2,5,1,1,6),_CpqCrPhyDrvStatus_Type())
cpqCrPhyDrvStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvStatus.setStatus(_A)
_CpqCrPhyDrvSize_Type=Integer32
_CpqCrPhyDrvSize_Object=MibTableColumn
cpqCrPhyDrvSize=_CpqCrPhyDrvSize_Object((1,3,6,1,4,1,232,141,2,5,1,1,7),_CpqCrPhyDrvSize_Type())
cpqCrPhyDrvSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvSize.setStatus(_A)
class _CpqCrPhyDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrPhyDrvCondition_Type.__name__=_C
_CpqCrPhyDrvCondition_Object=MibTableColumn
cpqCrPhyDrvCondition=_CpqCrPhyDrvCondition_Object((1,3,6,1,4,1,232,141,2,5,1,1,8),_CpqCrPhyDrvCondition_Type())
cpqCrPhyDrvCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvCondition.setStatus(_A)
class _CpqCrPhyDrvScsiID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrPhyDrvScsiID_Type.__name__=_C
_CpqCrPhyDrvScsiID_Object=MibTableColumn
cpqCrPhyDrvScsiID=_CpqCrPhyDrvScsiID_Object((1,3,6,1,4,1,232,141,2,5,1,1,9),_CpqCrPhyDrvScsiID_Type())
cpqCrPhyDrvScsiID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPhyDrvScsiID.setStatus(_A)
_CpqCrEMU_ObjectIdentity=ObjectIdentity
cpqCrEMU=_CpqCrEMU_ObjectIdentity((1,3,6,1,4,1,232,141,2,7))
class _CpqCrEMUBoardTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),('emuBoardTempNotInstalled',2),('emuBoardTempNormal',3),('emuBoardTempBelowNormal',4),('emuBoardTempAboveNormal',5),('emuBoardTempFarBelowNormal',6),('emuBoardTempFarAboveNormal',7),('emuBoardTempBackToNormal',8)))
_CpqCrEMUBoardTemperatureStatus_Type.__name__=_C
_CpqCrEMUBoardTemperatureStatus_Object=MibScalar
cpqCrEMUBoardTemperatureStatus=_CpqCrEMUBoardTemperatureStatus_Object((1,3,6,1,4,1,232,141,2,7,1),_CpqCrEMUBoardTemperatureStatus_Type())
cpqCrEMUBoardTemperatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUBoardTemperatureStatus.setStatus(_Q)
class _CpqCrEMUEnclosureTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),('emuEnclosureTempNotInstalled',2),('emuEnclosureTempNormal',3),('emuEnclosureTempBelowNormal',4),('emuEnclosureTempAboveNormal',5),('emuEnclosureTempFarBelowNormal',6),('emuEnclosureTempFarAboveNormal',7),('emuEnclosureTempBackToNormal',8)))
_CpqCrEMUEnclosureTemperatureStatus_Type.__name__=_C
_CpqCrEMUEnclosureTemperatureStatus_Object=MibScalar
cpqCrEMUEnclosureTemperatureStatus=_CpqCrEMUEnclosureTemperatureStatus_Object((1,3,6,1,4,1,232,141,2,7,2),_CpqCrEMUEnclosureTemperatureStatus_Type())
cpqCrEMUEnclosureTemperatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUEnclosureTemperatureStatus.setStatus(_Q)
class _CpqCrEMUBoardTemperatureLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrEMUBoardTemperatureLevel_Type.__name__=_C
_CpqCrEMUBoardTemperatureLevel_Object=MibScalar
cpqCrEMUBoardTemperatureLevel=_CpqCrEMUBoardTemperatureLevel_Object((1,3,6,1,4,1,232,141,2,7,3),_CpqCrEMUBoardTemperatureLevel_Type())
cpqCrEMUBoardTemperatureLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUBoardTemperatureLevel.setStatus(_Q)
class _CpqCrEMUEnclosureTemperatureLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrEMUEnclosureTemperatureLevel_Type.__name__=_C
_CpqCrEMUEnclosureTemperatureLevel_Object=MibScalar
cpqCrEMUEnclosureTemperatureLevel=_CpqCrEMUEnclosureTemperatureLevel_Object((1,3,6,1,4,1,232,141,2,7,4),_CpqCrEMUEnclosureTemperatureLevel_Type())
cpqCrEMUEnclosureTemperatureLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUEnclosureTemperatureLevel.setStatus(_Q)
class _CpqCrEMUCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrEMUCondition_Type.__name__=_C
_CpqCrEMUCondition_Object=MibScalar
cpqCrEMUCondition=_CpqCrEMUCondition_Object((1,3,6,1,4,1,232,141,2,7,5),_CpqCrEMUCondition_Type())
cpqCrEMUCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUCondition.setStatus(_A)
class _CpqCrEMUFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('emuFanOK',2),('emuFanCritical',3),('emuFanUnknown',4)))
_CpqCrEMUFanStatus_Type.__name__=_C
_CpqCrEMUFanStatus_Object=MibScalar
cpqCrEMUFanStatus=_CpqCrEMUFanStatus_Object((1,3,6,1,4,1,232,141,2,7,6),_CpqCrEMUFanStatus_Type())
cpqCrEMUFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUFanStatus.setStatus(_A)
class _CpqCrEMUFanCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrEMUFanCondition_Type.__name__=_C
_CpqCrEMUFanCondition_Object=MibScalar
cpqCrEMUFanCondition=_CpqCrEMUFanCondition_Object((1,3,6,1,4,1,232,141,2,7,7),_CpqCrEMUFanCondition_Type())
cpqCrEMUFanCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUFanCondition.setStatus(_A)
class _CpqCrEMUPowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('emuPwrSupplyOK',2),('emuPwrSupplyCritical',3),('emuPwrSupplyNotInstalled',4),('emuPwrSupplyUnknown',5)))
_CpqCrEMUPowerSupplyStatus_Type.__name__=_C
_CpqCrEMUPowerSupplyStatus_Object=MibScalar
cpqCrEMUPowerSupplyStatus=_CpqCrEMUPowerSupplyStatus_Object((1,3,6,1,4,1,232,141,2,7,8),_CpqCrEMUPowerSupplyStatus_Type())
cpqCrEMUPowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUPowerSupplyStatus.setStatus(_A)
class _CpqCrEMUPowerSupplyCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrEMUPowerSupplyCondition_Type.__name__=_C
_CpqCrEMUPowerSupplyCondition_Object=MibScalar
cpqCrEMUPowerSupplyCondition=_CpqCrEMUPowerSupplyCondition_Object((1,3,6,1,4,1,232,141,2,7,9),_CpqCrEMUPowerSupplyCondition_Type())
cpqCrEMUPowerSupplyCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUPowerSupplyCondition.setStatus(_A)
class _CpqCrEMUTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('emuTempOK',2),('emuTempCritical',3),('emuTempNonCritical',4),('emuTempUnknown',5)))
_CpqCrEMUTemperatureStatus_Type.__name__=_C
_CpqCrEMUTemperatureStatus_Object=MibScalar
cpqCrEMUTemperatureStatus=_CpqCrEMUTemperatureStatus_Object((1,3,6,1,4,1,232,141,2,7,10),_CpqCrEMUTemperatureStatus_Type())
cpqCrEMUTemperatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUTemperatureStatus.setStatus(_A)
class _CpqCrEMUTemperatureLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrEMUTemperatureLevel_Type.__name__=_C
_CpqCrEMUTemperatureLevel_Object=MibScalar
cpqCrEMUTemperatureLevel=_CpqCrEMUTemperatureLevel_Object((1,3,6,1,4,1,232,141,2,7,11),_CpqCrEMUTemperatureLevel_Type())
cpqCrEMUTemperatureLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUTemperatureLevel.setStatus(_A)
class _CpqCrEMUTemperatureCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrEMUTemperatureCondition_Type.__name__=_C
_CpqCrEMUTemperatureCondition_Object=MibScalar
cpqCrEMUTemperatureCondition=_CpqCrEMUTemperatureCondition_Object((1,3,6,1,4,1,232,141,2,7,12),_CpqCrEMUTemperatureCondition_Type())
cpqCrEMUTemperatureCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrEMUTemperatureCondition.setStatus(_A)
_CpqCrExpCab_ObjectIdentity=ObjectIdentity
cpqCrExpCab=_CpqCrExpCab_ObjectIdentity((1,3,6,1,4,1,232,141,2,8))
class _CpqCrExpCabPowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*((_F,1),('expCabPwrSupplyOK',2),('expCabPwrSupplyNonCritical',3),('expCabPwrSupplyUnknown',5)))
_CpqCrExpCabPowerSupplyStatus_Type.__name__=_C
_CpqCrExpCabPowerSupplyStatus_Object=MibScalar
cpqCrExpCabPowerSupplyStatus=_CpqCrExpCabPowerSupplyStatus_Object((1,3,6,1,4,1,232,141,2,8,1),_CpqCrExpCabPowerSupplyStatus_Type())
cpqCrExpCabPowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrExpCabPowerSupplyStatus.setStatus(_A)
class _CpqCrExpCabFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*((_F,1),('expCabFanOK',2),('expCabFanNonCritical',4),('expCabFanNotInstalled',5),('expCabFanUnknown',6)))
_CpqCrExpCabFanStatus_Type.__name__=_C
_CpqCrExpCabFanStatus_Object=MibScalar
cpqCrExpCabFanStatus=_CpqCrExpCabFanStatus_Object((1,3,6,1,4,1,232,141,2,8,2),_CpqCrExpCabFanStatus_Type())
cpqCrExpCabFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrExpCabFanStatus.setStatus(_A)
class _CpqCrExpCabTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('expCabTempOK',2),('expCabTempCritical',3),('expCabTempNonCritical',4),('expCabTempNotInstalled',5),('expCabTempUnknown',6)))
_CpqCrExpCabTemperatureStatus_Type.__name__=_C
_CpqCrExpCabTemperatureStatus_Object=MibScalar
cpqCrExpCabTemperatureStatus=_CpqCrExpCabTemperatureStatus_Object((1,3,6,1,4,1,232,141,2,8,3),_CpqCrExpCabTemperatureStatus_Type())
cpqCrExpCabTemperatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrExpCabTemperatureStatus.setStatus(_A)
class _CpqCrExpCabCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrExpCabCondition_Type.__name__=_C
_CpqCrExpCabCondition_Object=MibScalar
cpqCrExpCabCondition=_CpqCrExpCabCondition_Object((1,3,6,1,4,1,232,141,2,8,6),_CpqCrExpCabCondition_Type())
cpqCrExpCabCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrExpCabCondition.setStatus(_A)
class _CpqCrExpCabPowerSupplyCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrExpCabPowerSupplyCondition_Type.__name__=_C
_CpqCrExpCabPowerSupplyCondition_Object=MibScalar
cpqCrExpCabPowerSupplyCondition=_CpqCrExpCabPowerSupplyCondition_Object((1,3,6,1,4,1,232,141,2,8,7),_CpqCrExpCabPowerSupplyCondition_Type())
cpqCrExpCabPowerSupplyCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrExpCabPowerSupplyCondition.setStatus(_A)
class _CpqCrExpCabFanCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrExpCabFanCondition_Type.__name__=_C
_CpqCrExpCabFanCondition_Object=MibScalar
cpqCrExpCabFanCondition=_CpqCrExpCabFanCondition_Object((1,3,6,1,4,1,232,141,2,8,9),_CpqCrExpCabFanCondition_Type())
cpqCrExpCabFanCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrExpCabFanCondition.setStatus(_A)
class _CpqCrExpCabTemperatureCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrExpCabTemperatureCondition_Type.__name__=_C
_CpqCrExpCabTemperatureCondition_Object=MibScalar
cpqCrExpCabTemperatureCondition=_CpqCrExpCabTemperatureCondition_Object((1,3,6,1,4,1,232,141,2,8,10),_CpqCrExpCabTemperatureCondition_Type())
cpqCrExpCabTemperatureCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrExpCabTemperatureCondition.setStatus(_A)
_CpqCrPartition_ObjectIdentity=ObjectIdentity
cpqCrPartition=_CpqCrPartition_ObjectIdentity((1,3,6,1,4,1,232,141,2,9))
_CpqCrPartitionTable_Object=MibTable
cpqCrPartitionTable=_CpqCrPartitionTable_Object((1,3,6,1,4,1,232,141,2,9,1))
if mibBuilder.loadTexts:cpqCrPartitionTable.setStatus(_A)
_CpqCrPartitionEntry_Object=MibTableRow
cpqCrPartitionEntry=_CpqCrPartitionEntry_Object((1,3,6,1,4,1,232,141,2,9,1,1))
cpqCrPartitionEntry.setIndexNames((0,_G,_i),(0,_G,_j))
if mibBuilder.loadTexts:cpqCrPartitionEntry.setStatus(_A)
class _CpqCrPartitionLogDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrPartitionLogDrvIndex_Type.__name__=_C
_CpqCrPartitionLogDrvIndex_Object=MibTableColumn
cpqCrPartitionLogDrvIndex=_CpqCrPartitionLogDrvIndex_Object((1,3,6,1,4,1,232,141,2,9,1,1,1),_CpqCrPartitionLogDrvIndex_Type())
cpqCrPartitionLogDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPartitionLogDrvIndex.setStatus(_A)
class _CpqCrPartitionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqCrPartitionIndex_Type.__name__=_C
_CpqCrPartitionIndex_Object=MibTableColumn
cpqCrPartitionIndex=_CpqCrPartitionIndex_Object((1,3,6,1,4,1,232,141,2,9,1,1,2),_CpqCrPartitionIndex_Type())
cpqCrPartitionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPartitionIndex.setStatus(_A)
class _CpqCrPartitionRAIDLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('jbod',2),('raid0',3),('raid1',4),(_U,5),('raid4',6),('raid5',7)))
_CpqCrPartitionRAIDLevel_Type.__name__=_C
_CpqCrPartitionRAIDLevel_Object=MibTableColumn
cpqCrPartitionRAIDLevel=_CpqCrPartitionRAIDLevel_Object((1,3,6,1,4,1,232,141,2,9,1,1,3),_CpqCrPartitionRAIDLevel_Type())
cpqCrPartitionRAIDLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPartitionRAIDLevel.setStatus(_A)
class _CpqCrPartitionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('good',2),(_V,3),(_H,4),(_W,5),(_X,6)))
_CpqCrPartitionStatus_Type.__name__=_C
_CpqCrPartitionStatus_Object=MibTableColumn
cpqCrPartitionStatus=_CpqCrPartitionStatus_Object((1,3,6,1,4,1,232,141,2,9,1,1,4),_CpqCrPartitionStatus_Type())
cpqCrPartitionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPartitionStatus.setStatus(_A)
class _CpqCrPartitionSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqCrPartitionSize_Type.__name__=_C
_CpqCrPartitionSize_Object=MibTableColumn
cpqCrPartitionSize=_CpqCrPartitionSize_Object((1,3,6,1,4,1,232,141,2,9,1,1,5),_CpqCrPartitionSize_Type())
cpqCrPartitionSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPartitionSize.setStatus(_A)
class _CpqCrPartitionCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_H,4)))
_CpqCrPartitionCondition_Type.__name__=_C
_CpqCrPartitionCondition_Object=MibTableColumn
cpqCrPartitionCondition=_CpqCrPartitionCondition_Object((1,3,6,1,4,1,232,141,2,9,1,1,6),_CpqCrPartitionCondition_Type())
cpqCrPartitionCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqCrPartitionCondition.setStatus(_A)
_CpqCrTrap_ObjectIdentity=ObjectIdentity
cpqCrTrap=_CpqCrTrap_ObjectIdentity((1,3,6,1,4,1,232,141,3))
_CpqCrInterfaceTrap_ObjectIdentity=ObjectIdentity
cpqCrInterfaceTrap=_CpqCrInterfaceTrap_ObjectIdentity((1,3,6,1,4,1,232,141,3,1))
_CpqCrCntlrTrap_ObjectIdentity=ObjectIdentity
cpqCrCntlrTrap=_CpqCrCntlrTrap_ObjectIdentity((1,3,6,1,4,1,232,141,3,2))
_CpqCrLogDrvTrap_ObjectIdentity=ObjectIdentity
cpqCrLogDrvTrap=_CpqCrLogDrvTrap_ObjectIdentity((1,3,6,1,4,1,232,141,3,3))
_CpqCrSpareDrvTrap_ObjectIdentity=ObjectIdentity
cpqCrSpareDrvTrap=_CpqCrSpareDrvTrap_ObjectIdentity((1,3,6,1,4,1,232,141,3,4))
_CpqCrPhyDrvTrap_ObjectIdentity=ObjectIdentity
cpqCrPhyDrvTrap=_CpqCrPhyDrvTrap_ObjectIdentity((1,3,6,1,4,1,232,141,3,5))
_CpqCrEMUTrap_ObjectIdentity=ObjectIdentity
cpqCrEMUTrap=_CpqCrEMUTrap_ObjectIdentity((1,3,6,1,4,1,232,141,3,7))
_CpqCrExpCabTrap_ObjectIdentity=ObjectIdentity
cpqCrExpCabTrap=_CpqCrExpCabTrap_ObjectIdentity((1,3,6,1,4,1,232,141,3,8))
cpqCrController1FailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,2,0,1))
cpqCrController1FailureTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrController1FailureTrap.setStatus('')
cpqCrController1InformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,2,0,2))
cpqCrController1InformationTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrController1InformationTrap.setStatus('')
cpqCrController2FailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,2,0,3))
cpqCrController2FailureTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrController2FailureTrap.setStatus('')
cpqCrController2InformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,2,0,4))
cpqCrController2InformationTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrController2InformationTrap.setStatus('')
cpqCrLogDriveInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,3,0,5))
cpqCrLogDriveInformationTrap.setObjects(*((_D,_E),(_G,_K)))
if mibBuilder.loadTexts:cpqCrLogDriveInformationTrap.setStatus('')
cpqCrLogDriveFailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,3,0,6))
cpqCrLogDriveFailureTrap.setObjects(*((_D,_E),(_G,_K)))
if mibBuilder.loadTexts:cpqCrLogDriveFailureTrap.setStatus('')
cpqCrLogDriveReconstructTrap=NotificationType((1,3,6,1,4,1,232,141,3,3,0,7))
cpqCrLogDriveReconstructTrap.setObjects(*((_D,_E),(_G,_K)))
if mibBuilder.loadTexts:cpqCrLogDriveReconstructTrap.setStatus('')
cpqCrLogDriveReducedTrap=NotificationType((1,3,6,1,4,1,232,141,3,3,0,8))
cpqCrLogDriveReducedTrap.setObjects(*((_D,_E),(_G,_K)))
if mibBuilder.loadTexts:cpqCrLogDriveReducedTrap.setStatus('')
cpqCrLogDriveInitializingTrap=NotificationType((1,3,6,1,4,1,232,141,3,3,0,9))
cpqCrLogDriveInitializingTrap.setObjects(*((_D,_E),(_G,_K)))
if mibBuilder.loadTexts:cpqCrLogDriveInitializingTrap.setStatus('')
cpqCrDiskInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,10))
cpqCrDiskInformationTrap.setObjects(*((_D,_E),(_G,_P),(_G,_L)))
if mibBuilder.loadTexts:cpqCrDiskInformationTrap.setStatus('')
cpqCrDiskFailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,11))
cpqCrDiskFailureTrap.setObjects(*((_D,_E),(_G,_P),(_G,_L)))
if mibBuilder.loadTexts:cpqCrDiskFailureTrap.setStatus('')
cpqCrDiskReconstructTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,12))
cpqCrDiskReconstructTrap.setObjects(*((_D,_E),(_G,_L)))
if mibBuilder.loadTexts:cpqCrDiskReconstructTrap.setStatus('')
cpqCrDiskAvailableTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,13))
cpqCrDiskAvailableTrap.setObjects(*((_D,_E),(_G,_L)))
if mibBuilder.loadTexts:cpqCrDiskAvailableTrap.setStatus('')
cpqCrDiskSpareTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,14))
cpqCrDiskSpareTrap.setObjects(*((_D,_E),(_G,_L)))
if mibBuilder.loadTexts:cpqCrDiskSpareTrap.setStatus('')
cpqCrPhyDiskInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,30))
cpqCrPhyDiskInformationTrap.setObjects(*((_D,_E),(_G,_N)))
if mibBuilder.loadTexts:cpqCrPhyDiskInformationTrap.setStatus('')
cpqCrPhyDiskFailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,31))
cpqCrPhyDiskFailureTrap.setObjects(*((_D,_E),(_G,_N)))
if mibBuilder.loadTexts:cpqCrPhyDiskFailureTrap.setStatus('')
cpqCrPhyDiskReconstructTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,32))
cpqCrPhyDiskReconstructTrap.setObjects(*((_D,_E),(_G,_N)))
if mibBuilder.loadTexts:cpqCrPhyDiskReconstructTrap.setStatus('')
cpqCrPhyDiskAvailableTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,33))
cpqCrPhyDiskAvailableTrap.setObjects(*((_D,_E),(_G,_N)))
if mibBuilder.loadTexts:cpqCrPhyDiskAvailableTrap.setStatus('')
cpqCrPhyDiskSpareTrap=NotificationType((1,3,6,1,4,1,232,141,3,5,0,34))
cpqCrPhyDiskSpareTrap.setObjects(*((_D,_E),(_G,_k)))
if mibBuilder.loadTexts:cpqCrPhyDiskSpareTrap.setStatus('')
cpqCrEMUNormalTrap=NotificationType((1,3,6,1,4,1,232,141,3,7,0,15))
cpqCrEMUNormalTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrEMUNormalTrap.setStatus('')
cpqCrEMUFanFailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,7,0,16))
cpqCrEMUFanFailureTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrEMUFanFailureTrap.setStatus('')
cpqCrEMUFanInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,7,0,17))
cpqCrEMUFanInformationTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrEMUFanInformationTrap.setStatus('')
cpqCrEMUPowerSupplyFailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,7,0,18))
cpqCrEMUPowerSupplyFailureTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrEMUPowerSupplyFailureTrap.setStatus('')
cpqCrEMUPowerSupplyInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,7,0,19))
cpqCrEMUPowerSupplyInformationTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrEMUPowerSupplyInformationTrap.setStatus('')
cpqCrEMUTemperatureWarningTrap=NotificationType((1,3,6,1,4,1,232,141,3,7,0,23))
cpqCrEMUTemperatureWarningTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrEMUTemperatureWarningTrap.setStatus('')
cpqCrEMUTemperatureCriticalTrap=NotificationType((1,3,6,1,4,1,232,141,3,7,0,24))
cpqCrEMUTemperatureCriticalTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrEMUTemperatureCriticalTrap.setStatus('')
cpqCrEMUTemperatureInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,7,0,25))
cpqCrEMUTemperatureInformationTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrEMUTemperatureInformationTrap.setStatus('')
cpqCrExpCabFanFailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,8,0,20))
cpqCrExpCabFanFailureTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrExpCabFanFailureTrap.setStatus('')
cpqCrExpCabFanInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,8,0,21))
cpqCrExpCabFanInformationTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrExpCabFanInformationTrap.setStatus('')
cpqCrExpCabPowerSupplyFailureTrap=NotificationType((1,3,6,1,4,1,232,141,3,8,0,22))
cpqCrExpCabPowerSupplyFailureTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrExpCabPowerSupplyFailureTrap.setStatus('')
cpqCrExpCabTemperatureWarningTrap=NotificationType((1,3,6,1,4,1,232,141,3,8,0,26))
cpqCrExpCabTemperatureWarningTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrExpCabTemperatureWarningTrap.setStatus('')
cpqCrExpCabTemperatureCriticalTrap=NotificationType((1,3,6,1,4,1,232,141,3,8,0,27))
cpqCrExpCabTemperatureCriticalTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrExpCabTemperatureCriticalTrap.setStatus('')
cpqCrExpCabTemperatureInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,8,0,28))
cpqCrExpCabTemperatureInformationTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrExpCabTemperatureInformationTrap.setStatus('')
cpqCrExpCabPowerSupplyInformationTrap=NotificationType((1,3,6,1,4,1,232,141,3,8,0,29))
cpqCrExpCabPowerSupplyInformationTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:cpqCrExpCabPowerSupplyInformationTrap.setStatus('')
mibBuilder.exportSymbols(_G,**{'cpqClusteredRAID':cpqClusteredRAID,'cpqCrMibRev':cpqCrMibRev,'cpqCrMibRevMajor':cpqCrMibRevMajor,'cpqCrMibRevMinor':cpqCrMibRevMinor,'cpqCrMibCondition':cpqCrMibCondition,'cpqCrComponent':cpqCrComponent,'cpqCrInterface':cpqCrInterface,'cpqCrOsCommon':cpqCrOsCommon,'cpqCrOsCommonPollFreq':cpqCrOsCommonPollFreq,'cpqCrCntlr':cpqCrCntlr,'cpqCrCntlrTable':cpqCrCntlrTable,'cpqCrCntlrEntry':cpqCrCntlrEntry,_S:cpqCrCntlrIndex,'cpqCrCntlrSerialNumber':cpqCrCntlrSerialNumber,'cpqCrCntlrFWRev':cpqCrCntlrFWRev,'cpqCrCntlrCondition':cpqCrCntlrCondition,'cpqCrCntlrCurrentRole':cpqCrCntlrCurrentRole,'cpqCrCntlrDriveOwnership':cpqCrCntlrDriveOwnership,'cpqCrCntlrRebuildRate':cpqCrCntlrRebuildRate,'cpqCrCntlrCreateRate':cpqCrCntlrCreateRate,'cpqCrCntlrCacheSize':cpqCrCntlrCacheSize,'cpqCrCntlrSimmSizeA':cpqCrCntlrSimmSizeA,'cpqCrCntlrSimmSizeB':cpqCrCntlrSimmSizeB,'cpqCrLogDrv':cpqCrLogDrv,'cpqCrLogDrvTable':cpqCrLogDrvTable,'cpqCrLogDrvEntry':cpqCrLogDrvEntry,_T:cpqCrLogDrvCntlrIndex,_K:cpqCrLogDrvIndex,'cpqCrLogDrvRAIDLevel':cpqCrLogDrvRAIDLevel,'cpqCrLogDrvStatus':cpqCrLogDrvStatus,'cpqCrLogDrvRebuildPercentage':cpqCrLogDrvRebuildPercentage,'cpqCrLogDrvAvailSpares':cpqCrLogDrvAvailSpares,'cpqCrLogDrvSize':cpqCrLogDrvSize,'cpqCrLogDrvPhyDrvIDs':cpqCrLogDrvPhyDrvIDs,'cpqCrLogDrvCondition':cpqCrLogDrvCondition,'cpqCrLogDrvPartitionIDs':cpqCrLogDrvPartitionIDs,'cpqCrSpareDrv':cpqCrSpareDrv,'cpqCrSpareTable':cpqCrSpareTable,'cpqCrSpareEntry':cpqCrSpareEntry,_Y:cpqCrSpareCntlrIndex,_Z:cpqCrSparePhyDrvIndex,'cpqCrSpareStatus':cpqCrSpareStatus,'cpqCrSpareCondition':cpqCrSpareCondition,_k:cpqCrSpareScsiID,'cpqCrPhyDrv':cpqCrPhyDrv,'cpqCrPhyDrvTable':cpqCrPhyDrvTable,'cpqCrPhyDrvEntry':cpqCrPhyDrvEntry,_P:cpqCrPhyDrvCntlrIndex,_L:cpqCrPhyDrvIndex,'cpqCrPhyDrvVendor':cpqCrPhyDrvVendor,'cpqCrPhyDrvModel':cpqCrPhyDrvModel,'cpqCrPhyDrvRevision':cpqCrPhyDrvRevision,'cpqCrPhyDrvStatus':cpqCrPhyDrvStatus,'cpqCrPhyDrvSize':cpqCrPhyDrvSize,'cpqCrPhyDrvCondition':cpqCrPhyDrvCondition,_N:cpqCrPhyDrvScsiID,'cpqCrEMU':cpqCrEMU,'cpqCrEMUBoardTemperatureStatus':cpqCrEMUBoardTemperatureStatus,'cpqCrEMUEnclosureTemperatureStatus':cpqCrEMUEnclosureTemperatureStatus,'cpqCrEMUBoardTemperatureLevel':cpqCrEMUBoardTemperatureLevel,'cpqCrEMUEnclosureTemperatureLevel':cpqCrEMUEnclosureTemperatureLevel,'cpqCrEMUCondition':cpqCrEMUCondition,'cpqCrEMUFanStatus':cpqCrEMUFanStatus,'cpqCrEMUFanCondition':cpqCrEMUFanCondition,'cpqCrEMUPowerSupplyStatus':cpqCrEMUPowerSupplyStatus,'cpqCrEMUPowerSupplyCondition':cpqCrEMUPowerSupplyCondition,'cpqCrEMUTemperatureStatus':cpqCrEMUTemperatureStatus,'cpqCrEMUTemperatureLevel':cpqCrEMUTemperatureLevel,'cpqCrEMUTemperatureCondition':cpqCrEMUTemperatureCondition,'cpqCrExpCab':cpqCrExpCab,'cpqCrExpCabPowerSupplyStatus':cpqCrExpCabPowerSupplyStatus,'cpqCrExpCabFanStatus':cpqCrExpCabFanStatus,'cpqCrExpCabTemperatureStatus':cpqCrExpCabTemperatureStatus,'cpqCrExpCabCondition':cpqCrExpCabCondition,'cpqCrExpCabPowerSupplyCondition':cpqCrExpCabPowerSupplyCondition,'cpqCrExpCabFanCondition':cpqCrExpCabFanCondition,'cpqCrExpCabTemperatureCondition':cpqCrExpCabTemperatureCondition,'cpqCrPartition':cpqCrPartition,'cpqCrPartitionTable':cpqCrPartitionTable,'cpqCrPartitionEntry':cpqCrPartitionEntry,_i:cpqCrPartitionLogDrvIndex,_j:cpqCrPartitionIndex,'cpqCrPartitionRAIDLevel':cpqCrPartitionRAIDLevel,'cpqCrPartitionStatus':cpqCrPartitionStatus,'cpqCrPartitionSize':cpqCrPartitionSize,'cpqCrPartitionCondition':cpqCrPartitionCondition,'cpqCrTrap':cpqCrTrap,'cpqCrInterfaceTrap':cpqCrInterfaceTrap,'cpqCrCntlrTrap':cpqCrCntlrTrap,'cpqCrController1FailureTrap':cpqCrController1FailureTrap,'cpqCrController1InformationTrap':cpqCrController1InformationTrap,'cpqCrController2FailureTrap':cpqCrController2FailureTrap,'cpqCrController2InformationTrap':cpqCrController2InformationTrap,'cpqCrLogDrvTrap':cpqCrLogDrvTrap,'cpqCrLogDriveInformationTrap':cpqCrLogDriveInformationTrap,'cpqCrLogDriveFailureTrap':cpqCrLogDriveFailureTrap,'cpqCrLogDriveReconstructTrap':cpqCrLogDriveReconstructTrap,'cpqCrLogDriveReducedTrap':cpqCrLogDriveReducedTrap,'cpqCrLogDriveInitializingTrap':cpqCrLogDriveInitializingTrap,'cpqCrSpareDrvTrap':cpqCrSpareDrvTrap,'cpqCrPhyDrvTrap':cpqCrPhyDrvTrap,'cpqCrDiskInformationTrap':cpqCrDiskInformationTrap,'cpqCrDiskFailureTrap':cpqCrDiskFailureTrap,'cpqCrDiskReconstructTrap':cpqCrDiskReconstructTrap,'cpqCrDiskAvailableTrap':cpqCrDiskAvailableTrap,'cpqCrDiskSpareTrap':cpqCrDiskSpareTrap,'cpqCrPhyDiskInformationTrap':cpqCrPhyDiskInformationTrap,'cpqCrPhyDiskFailureTrap':cpqCrPhyDiskFailureTrap,'cpqCrPhyDiskReconstructTrap':cpqCrPhyDiskReconstructTrap,'cpqCrPhyDiskAvailableTrap':cpqCrPhyDiskAvailableTrap,'cpqCrPhyDiskSpareTrap':cpqCrPhyDiskSpareTrap,'cpqCrEMUTrap':cpqCrEMUTrap,'cpqCrEMUNormalTrap':cpqCrEMUNormalTrap,'cpqCrEMUFanFailureTrap':cpqCrEMUFanFailureTrap,'cpqCrEMUFanInformationTrap':cpqCrEMUFanInformationTrap,'cpqCrEMUPowerSupplyFailureTrap':cpqCrEMUPowerSupplyFailureTrap,'cpqCrEMUPowerSupplyInformationTrap':cpqCrEMUPowerSupplyInformationTrap,'cpqCrEMUTemperatureWarningTrap':cpqCrEMUTemperatureWarningTrap,'cpqCrEMUTemperatureCriticalTrap':cpqCrEMUTemperatureCriticalTrap,'cpqCrEMUTemperatureInformationTrap':cpqCrEMUTemperatureInformationTrap,'cpqCrExpCabTrap':cpqCrExpCabTrap,'cpqCrExpCabFanFailureTrap':cpqCrExpCabFanFailureTrap,'cpqCrExpCabFanInformationTrap':cpqCrExpCabFanInformationTrap,'cpqCrExpCabPowerSupplyFailureTrap':cpqCrExpCabPowerSupplyFailureTrap,'cpqCrExpCabTemperatureWarningTrap':cpqCrExpCabTemperatureWarningTrap,'cpqCrExpCabTemperatureCriticalTrap':cpqCrExpCabTemperatureCriticalTrap,'cpqCrExpCabTemperatureInformationTrap':cpqCrExpCabTemperatureInformationTrap,'cpqCrExpCabPowerSupplyInformationTrap':cpqCrExpCabPowerSupplyInformationTrap})